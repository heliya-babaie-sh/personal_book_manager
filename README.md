# Personal Book Mananger 

A simple  book manager built with  ![Static Badge](https://img.shields.io/badge/python-96cef5?logo=python&logoColor=blue)

## Features
- Add multiple book 
- Saves books
- loads saved books
- admin mode
- set task priority

## Task priority 
Each task can have one of this priority levele:
- low
- medium
- high

## Requirements
- `python 3`
- `python-dotenv`

## Installation
install the required packages:
```bash
pip install -r requirements.txt
```

## Environment Setup
create a `.env` file in the project folde
Use `.env.example` as a templet
Add your admin password 
```env
BOOK_MANAGER_ADMIN_PASSWORD=your_password
```
replaace `your_passport` with your own admin password

## run the program 
run the main file:

```bash 
python main.py
```


## screen shot
![personal_book_manager_screenshot](image\Screenshot.png)

## Demo
![personal_book_manager_demo](\gift\demo.gif)


## File Description 
| File | Description | 
| --- | --- | 
| ` main.py ` | main file used to run book manager |
| `  books.py ` | getting list of book titles |
| `requirements.txt` |Contains a list of the Python libraries and dependencies required to run the project. |
| `.env.example ` | shows the environment variables needed by the project |
| `.gitignore ` |Contains a list of the Python libraries and dependencies required to run the project. |
| `.README.md ` | contains the project documentation |
| `image/ ` | stores project screenshots |   
| `image/screenshot.png ` | screenshot of the  start program |
| `gift/ ` | stores demo GIF files |
| `gift/demo.gif ` | shows the project demo |



## How it works
> First, we ask you to enter your name. Then, we ask whether you are an admin or not. If you have the correct password, we can identify you as an admin. In the next step, we ask how many books you want to add. You must enter the names of the books according to the number you selected. Finally, the book names will be saved and displayed to you.


## Troubleshooting

### 1. FileNotFoundError

- **Problem:** The program cannot find the file.

- **Possible Cause:** The file does not exist.

- **How to Check:** Check if the file exists in the project folder.

### 2. JSONDecodeError

- **Problem:** The program cannot read the books.json file.

- **Possible Cause:** The file is empty or contains incorrect data.

- **How to Check:** Open books.json and check its contents.

### 3. ModuleNotFoundError

- **Problem:** The program cannot find the required module.

- **Possible Cause:** The module is not installed.

- **How to Check:** Check if the required module is installed.

### 4. Admin Password Error

- **Problem:** The admin password is not working.

- **Possible Cause:** The password in the .env file is incorrect.

- **How to Check:** Check the password in the .env file.


