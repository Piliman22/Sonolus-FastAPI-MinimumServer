from main import sonolus

import time
from sonolus_fastapi.utils.context import SonolusContext
from sonolus_fastapi.model.Response.authenticate import ServerAuthenticateResponse
from sonolus_fastapi.utils.generate import generate_random_string

@sonolus.server.authenticate(ServerAuthenticateResponse) # 認証ハンドラーを登録 Register authenticate handler
async def authenticate(ctx: SonolusContext): # 認証処理 Authentication process
    session = generate_random_string(16) # セッションIDを生成 Generate session ID
    expiration = int(time.time() * 1000) + 3600 * 1000 # 有効期限を1時間後に設定 Set expiration to 1 hour later
    
    return ServerAuthenticateResponse( # 認証レスポンスを返す Return authentication response
        session=session, # セッションID Session ID
        expiration=expiration, # 有効期限 Expiration
    )