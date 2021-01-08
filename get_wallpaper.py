import requests
import datetime
import os
import win32api,win32gui,win32con


global img_path
img_path = ''
def get_picture():
    url = 'https://api.berryapi.net/?service=App.Bing.Images&w=1920&h=1080&day=-0'
    print('正在下载今日bing的壁纸中......默认分辨率为1920*1080')
    response = requests.get(url)
    #请求今日必应的图片 ,分辨率为1920*1080

    picture = response.content
    path = 'D:\wallpaper'

    date = datetime.datetime.now().strftime('%Y-%m-%d')

    try:
        if not os.path.exists(path):
            print('没有找到图片的保存路径',path,'已经自动创建')
            os.makedirs(path)
        with open(path+'\\'+date+'.jpg','wb') as f:
            f.write(picture)
            print(date,'的壁纸下载成功，图片的路径为',path+date+'.jpg')
            global img_path
            img_path = path+'\\'+date+'.jpg'
            print(img_path)
    except:
        print('程序出错 请联系我')


def set_wallpaper(img_path):
    print()
    # 打开指定注册表路径
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 最后的参数:2拉伸,0居中,6适应,10填充,0平铺
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数:1表示平铺,拉伸居中等都是0
    win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, img_path, win32con.SPIF_SENDWININICHANGE)


if __name__ == '__main__':
    get_picture()
    set_wallpaper(img_path)