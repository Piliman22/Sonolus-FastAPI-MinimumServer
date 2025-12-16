from main import sonolus

from sonolus_fastapi.model.base import SonolusServerInfo, SonolusConfiguration, SonolusButton, SonolusButtonType
from sonolus_fastapi.utils.context import SonolusContext

@sonolus.server.server_info(SonolusServerInfo)
async def get_server_info(ctx: SonolusContext) -> SonolusServerInfo: 
    return SonolusServerInfo(
        title="Minimum Sonolus-FastAPI Server",
        description="A minimal example of Sonolus-FastAPI server implementation.",
        buttons=[
            SonolusButton(type=SonolusButtonType.AUTHENTICATION),
        ],
        configuration=SonolusConfiguration(
            options=[]
        ),
        banner=None,
    )