from telethon import events, Button


async def start_srb(event, st):
    await event.reply(
        st,
        buttons=[
            [
                Button.inline("📸 Set Thumbnail", data="set"),
                Button.inline("🗑 Remove Thumbnail", data="rem")
            ],
            [
                Button.url("👨‍💻 Developer", url="t.me/GenXNano")
            ]
        ]
    )


async def vc_menu(event):
    await event.edit(
        "**🎥 Video Converter v1.4**",
        buttons=[
            [
                Button.inline("ℹ️ Info", data="info"),
                Button.inline("📦 Source", data="source")
            ],
            [
                Button.inline("📢 Notice", data="notice"),
                Button.inline("🏠 Main Menu", data="help")
            ],
            [
                Button.url("👨‍💻 Developer", url="t.me/GenXNano")
            ]
        ]
    )
