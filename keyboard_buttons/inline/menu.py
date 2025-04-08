from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline tugmalar
inline_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Qayta yuklash", callback_data="reload")],
        [InlineKeyboardButton(text="📤 Do‘stlarga yuborish", switch_inline_query="")],
        # [InlineKeyboardButton(text="💬 Kanal", url="https://t.me/your_channel")],
    ]
)
