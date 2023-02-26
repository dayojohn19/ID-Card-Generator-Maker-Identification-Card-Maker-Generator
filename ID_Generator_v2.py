from PIL import Image, ImageDraw, ImageFont,ImageFilter
import os
import pyqrcode

class Generate_ID:
    def __init__(self, USER_ID, USER_NAME, USER_URL, USER_MEMBER_TYPE, USER_MEMBER_DATE):
        self.USER_ID = USER_ID
        self.workingPath = self.pathFiles(USER_ID,USER_NAME)
        self.USER_URL = USER_URL
        self.MEMBER_TYPE = USER_MEMBER_TYPE
        self.MEMBER_DATE = USER_MEMBER_DATE
        self.USER_NAME = USER_NAME
        self.BACKGROUND_IMAGE = 'transparent.png'        
        
        
        self.card_container = self.background_ID(USER_NAME)
        return
        self.filename = ID_FILE_NAME
        


    def pathFiles(self,userID,userName):
        pathExists = os.getcwd()+'/ID_Credentials'+'/'+userID+'/'+userName
        if not os.path.exists(pathExists):
            pathExists = os.makedirs(pathExists)
        return pathExists

        

    def background_ID(self,user_name):
        imageBackground = Image.new('RGB',(1000,600),(210,	191,	158	))
        
        imageBackground = self.add_rectangecolor(imageBackground)
        imageBackground =self.put_backgroundimage(imageBackground)
        imageBackground = self.Make_roundcorners(imageBackground, 40)
        imageBackground = self.write_texts(imageBackground)
        imageBackground = self.upload_picture(imageBackground)
        imageBackground.save(self.workingPath+'/'+self.USER_ID+'.png')
        return imageBackground


    def upload_picture(self, im):
        profilePhoto = Image.open(os.getcwd()+'/Profile_Photos/'+self.USER_ID+'.png')
        newProfP = profilePhoto.resize((300,300),Image.LANCZOS)
        im.paste(newProfP,(90,130))
        qr_logo_path = self.share_qr_code()
        qr_logo = Image.open(qr_logo_path)
        qr_logo = qr_logo.resize((250,250),Image.LANCZOS)

        im.paste(qr_logo,(575,250))
        return im

    def share_qr_code(self):
        url = pyqrcode.QRCode(self.USER_URL, error='H')
        url.png(self.workingPath+'/QR_Code.png',scale=10)
        # Saving QR CODE URL
        im = Image.open(self.workingPath+'/QR_Code.png')
        im = im.convert("RGBA")
        logo = Image.open(os.getcwd()+'/CarPoolLogo.png')
        x,y = im.size
        a,s= logo.size
        region = ((x//2)-(a//2)),((y//2)-(s//2))
        im.paste(logo,region)
        im.save(self.workingPath+'/QR_Code.png')
        return self.workingPath+'/QR_Code.png'


    def write_texts(self,im):
        toDraw = ImageDraw.Draw(im)
        Company_Name = 'Filipino Transportation \n Carpooling'
        user_url = self.USER_URL
        comany_color = 'rgb(242,237,223)'
        # comany_color = 'rgb(51, 117, 193)'  # black color
        font = ImageFont.truetype(os.getcwd()+'/fontsCustom/Aller_Bd.ttf', size=50)
        Name_font = ImageFont.truetype(os.getcwd()+'/fontsCustom/Aller_Bd.ttf', size=45)
        member_type = ImageFont.truetype(os.getcwd()+'/fontsCustom/Aller_Bd.ttf', size=30)
        toDraw.text((700,90), Company_Name, fill=comany_color, font=font,align='center', anchor='ms')
        toDraw.text((235,500), self.USER_NAME, fill=comany_color, font=Name_font,align='center', anchor='ms')
        toDraw.text((245,540), self.MEMBER_TYPE, fill=comany_color, font=member_type,align='center',anchor='ms')
        toDraw.text((705,540), user_url, fill=comany_color, font=member_type,align='center',anchor='ms')
        toDraw.text((190,70), 'Member since: \n'+self.MEMBER_DATE, fill=comany_color, font=member_type,align='left',anchor='ms')
        # toDraw.multiline_text((75,500), texts,fill=None, font=None, anchor=None, spacing=4, align='left', direction=None, features=None, language=None, stroke_width=0, stroke_fill=None, embedded_color=False)

        # toDraw  .draw(toDraw)
        return im

    def put_backgroundimage(self, im):
        
        imageObject = Image.open(os.getcwd()+'/'+self.BACKGROUND_IMAGE)
        # imageObject = imageObject.convert("L")
        # imageObject = imageObject.filter(ImageFilter.FIND_EDGES)
        imageObject = imageObject.filter(ImageFilter.EMBOSS)
        # imageObject.filter(ImageFilter.SMOOTH)
        # imageObject.save(self.workingPath+'/'+self.BACKGROUND_IMAGE)
        # imageObject = Image.open(self.workingPath+'/'+self.BACKGROUND_IMAGE)
        imageObject.putalpha(150)
        
        

        im.paste(imageObject,(0,0),imageObject)  
        return im
    def Make_roundcorners(self, im, rad):
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', im.size, 255)
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im
    def add_rectangecolor(self, im):
        colorToAdd = Image.new('RGB', (1000, 185), (50	,94	,153	))
        im.paste(colorToAdd, (0,0))
        colorToAdd = Image.new('RGB', (1000, 50), (127	,49	,72		))
        im.paste(colorToAdd, (0,185))
        return im

x = Generate_ID('12', 'John Doe','https://treep.today/view/12','Associate Member','Feb 26, 2023')