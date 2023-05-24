from __future__ import annotations

import asyncio

from azure.core.exceptions import ClientAuthenticationError
from kiota_abstractions.api_error import APIError
from loguru import logger

from mirsg_project_manager.config import client, consent_url

REQUEST_TIMEOUT_SECONDS = 10


async def get_site_folders_sdk(drive_id):
    try:
        items = (
            await client.drives.by_drive_id(drive_id)
            .items.by_drive_item_id("01KJZMKAB7MQKTYIPKJZGKVQ7FD4VPSHA2")
            .children.get()
        )
        if items and items.value:
            projects = {}
            for item in items.value:
                projects[item.id] = {"name": item.name, "url": item.web_url}
            return projects
    except APIError as e:
        logger.error(e.error.message)


def get_site_folders(drive_id):
    try:
        projects = asyncio.run(get_site_folders_sdk(drive_id))
        logger.success("Done")
        return projects
    except ClientAuthenticationError:
        logger.info(
            "If consent hasn't been given to this application before, navigate to this url:\n{consent_url}",
            consent_url=consent_url,
        )
        return None
