from sonolus_fastapi import Sonolus

sonolus = Sonolus(
    address="https://sonolus-fastapi.pim4n-net.com/demo/minimum",
    port=8010
)

from handler import * # ハンドラーのインポート Import handlers

if __name__ == "__main__":
    sonolus.run()