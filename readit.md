# ID Card Generator, Maker / Identification Card Maker, Generator

> ## Step 3: Run the following commands
>
>        pip3 install -r requirements.txt
>
> ---
>
>        Generate_ID(USER_ID, USER_NAME, USER_URL, USER_MEMBER_TYPE, USER_MEMBER_DATE)
>
> ---

## Step 2: Edit Values

- ### Put Card Holder Photo [in this Folder](/Profile_Photos/) and name it `USER_ID.png`

> ## Editable Area
>
> - `USER_ID` is the generated [Folder](/ID_Credentials/12/) inside ID_Credentials
> - `USER_NAME` UserName
> - `USER_URL` QR CODE URL on the CARD
> - `MEMBER_TYPE` = Associate Member
> - `MEMBER_DATE` = Feb 26,2023
>   ***
> - [Background Image](/transparent.png) replace the file of your desired Background Image
>   - should be named as `transparent.png`
>   - You can change background mask design under `def put_backgroundimage` change the `ImageFilter...`[Check this link for more][1]
> - [Fonts](/fontsCustom/) You can download fonts and put here and change `fontsCustom/Aller_Bd.ttf`

---

[1]: (https://realpython.com/image-processing-with-the-python-pillow-library/) "Check here"

## Step 4 Saved Files in Folders

> ## All files wii be saved in
>
> - ID_Credentials/` USER_ID`/` USERNAME`/ [here](/ID_Credentials/
> - the ID CARD will be named on the same folder as
>   ## `USER_ID.png`

![Voilla Ready for Scan](/ID_Credentials/12/John%20Doe/12.png "Voilla Ready for Scan")
