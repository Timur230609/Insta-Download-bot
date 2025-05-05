# import os
# import requests
# from aiogram.types import Message, FSInputFile
# from loader import dp
# from keyboard_buttons.inline.menu import inline_buttons
# from aiogram import F
# from aiogram.types import FSInputFile, Message
# import instaloader
# # from pytube import YouTube
# # from tiktok_downloader import snaptik
# import requests
# # import yt_dlp
# from loader import dp, bot
# from keyboard_buttons.inline.menu import inline_buttons
# # import asyncio
# # import tempfile
# # from bs4 import BeautifulSoup
# @dp.message(F.chat.func(lambda chat: chat.type == "private"))
# async def handle_link(message: Message):
#     post = message.text.strip()
    
#     if "instagram.com" in post:
#         await download_instagram_content(message, post)
        
#     # elif "pinterest.com" in post:
#     #     await download_pinterest_content(message, post)
    
#     # elif "youtube.com" in post:
#     #     await download_youtube_content(message, post)
        
#     # elif "tiktok.com" in post:
#     #     await download_tiktok_content(message, post)
        
#     else:
#         await message.reply("Havola nomini tug'ri kiriting ❗️")

# # '''=========================================================================================================================================''' 

# # Instagram video yuklash
# @dp.message(F.chat.func(lambda chat: chat.type == "private"))
# async def handle_link(message: Message):
#     post = message.text.strip()

#     if "instagram.com" in post:
#         await download_instagram_content(message, post)
#     else:
#         await message.reply("Havola nomini tug'ri kiriting ❗️")
# async def download_instagram_content(message: Message, url: str):
#     delet_message = await message.answer("⌛️")
        
#     loader = instaloader.Instaloader()
#     shortcode = url.split("/")[-2] 
#     post = instaloader.Post.from_shortcode(loader.context, shortcode)  # Instagram postini olish

#     if post.is_video:
#         video_url = post.video_url  
#         video_data = requests.get(video_url).content 

#         with open("instagram_video.mp4", "wb") as file:
#             file.write(video_data)

#         await message.answer_video(video=FSInputFile("instagram_video.mp4"), caption="📥 @ orqali yuklab olindi", reply_markup=inline_buttons)

#         os.remove("instagram_video.mp4")
    
#     elif post.is_image:
#         image_url = post.url  
#         image_data = requests.get(image_url).content 
        
#         with open("instagram_image.jpg", "wb") as file:
#             file.write(image_data)
        
#         await message.answer_photo(photo=FSInputFile("instagram_image.jpg"), caption="📥 orqali yuklab olindi", reply_markup=inline_buttons)

#         os.remove("instagram_image.jpg")
#     else:
#         await message.reply("Ushbu havola videoga yoki rasminga tegishli emas ❗️")
        
#     await delet_message.delete()

# '''=========================================================================================================================================''' 

# # # API sozlamalari
# # API_URL = "https://pinterestapi.example.com/api/v1/download"
# # API_TOKEN = "YOUR_SECRET_API_TOKEN"

# # @dp.message(lambda message: "pinterest.com" in message.text)
# # async def handle_pinterest(message: Message):
# #     url = message.text.strip()
# #     loading_msg = await message.answer("⌛️ Pinterest havolasi tekshirilmoqda...")

# #     try:
# #         headers = {
# #             "Authorization": f"Bearer {API_TOKEN}",
# #             "Accept": "application/json"
# #         }
# #         params = {"url": url}

# #         response = requests.get(API_URL, headers=headers, params=params)
# #         response.raise_for_status()
# #         data = response.json()

# #         if data.get("status") != "success":
# #             await message.reply("❗️ Yuklab olishda xatolik yuz berdi.")
# #             return

# #         media_url = data.get("media_url")
# #         if not media_url:
# #             await message.reply("❗️ Media havola topilmadi.")
# #             return

# #         filename = "pinterest_video.mp4" if media_url.endswith(".mp4") else "pinterest_image.jpg"
# #         media_data = requests.get(media_url).content

# #         with open(filename, "wb") as f:
# #             f.write(media_data)

# #         if filename.endswith(".mp4"):
# #             await message.answer_video(FSInputFile(filename), caption="📥 Pinterestdan video yuklandi", reply_markup=inline_buttons)
# #         else:
# #             await message.answer_photo(FSInputFile(filename), caption="📥 Pinterestdan rasm yuklandi", reply_markup=inline_buttons)

# #         os.remove(filename)

# #     except Exception as e:
# #         await message.reply(f"❌ Xatolik yuz berdi: {e}")

# #     await loading_msg.delete()

# '''========================================================================================================================================='''

# # # Pinterest video yuklash
# # async def download_pinterest_content(message: Message, url: str):
# #     delet_message = await message.answer("⌛ Video yuklanmoqda...")
# #     post = message.text.strip()
# #     loader = instaloader.Instaloader()
# #     shortcode = url.split("/")[-2] 
# #     post = instaloader.Post.from_shortcode(loader.context, shortcode)  # Instagram postini olish

# #     # try:
# #     #     headers = {"User-Agent": "Mozilla/5.0"}
# #     #     response = requests.get(url, headers=headers)
# #     #     soup = BeautifulSoup(response.text, "html.parser")
# #     #     video_tag = soup.find("video")

# #     if post.is_video:
# #         video_url = post.video_url  
# #         video_data = requests.get(video_url).content 
    
# #         with open("pinterest_video.mp4", "wb") as file:
# #                 file.write(video_data)
    
# #         await message.answer_video(video=FSInputFile("pinterest_video.mp4"), caption="📥 @ orqali yuklab olindi", reply_markup=inline_buttons)
    
# #         os.remove("pinterest_video.mp4")
     
# #     elif post.is_image:
# #         image_url = post.url  
# #         image_data = requests.get(image_url).content 
          
# #         with open("pinterest_image.jpg", "wb") as file:
# #             file.write(image_data)
          
# #         await message.answer_photo(photo=FSInputFile("pinterest_image.jpg"), caption="📥 orqali yuklab olindi", reply_markup=inline_buttons)
    
# #         os.remove("pinterest_image.jpg")
# #     else:
# #         await message.reply("Ushbu havola videoga yoki rasminga tegishli emas ❗️")
        
# #     await delet_message.delete()    

# '''=========================================================================================================================================''' 

# # # You Tube video yuklash
# # async def download_youtube_content(url):
# #     ydl_opts = {
# #         'format': 'best',
# #         'outtmpl': 'youtube_video.mp4',
# #     }
# #     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
# #         ydl.download([url])
# #     return "youtube_video.mp4"

# '''========================================================================================================================================='''
# url = "https://tiktok-download-video1.p.rapidapi.com/getVideo"

# def tiktok_save(link):
#   querystring = {"url":link,"hd":"1"}

#   headers = {
#     "X-RapidAPI-Key": "90de015fedmsh6cb4b8ec8899b66p10b5c6jsn95e5205d74bc",
#     "X-RapidAPI-Host": "tiktok-download-video1.p.rapidapi.com"
#   }

#   response = requests.get(url, headers=headers, params=querystring)
#   data = {}
#   try:
#     data["music"] = response.json()["data"]["music"]
#   except:
#     pass
#   try:
#     data["video"] = response.json()["data"]["hdplay"]
#   except:
#     pass
#   try:
#     data["images"] = response.json()["data"]["images"]
#   except:
#     pass
#   return data