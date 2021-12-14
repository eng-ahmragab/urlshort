# urlshort
A simple tool built to help you shorten long urls or upload and share pictures with prettier shortened urls.





# Features:
- Shorten long URLs into a custom short name of your choice.
- Upload Pictures and shorten their URLs.
- Ability to check your recently created short URLs.

![App Screenshot](https://i.ibb.co/VWDVFqf/screenshot.png)



# Development Setup
1) On the root directory, create a file: .env
2) Add the needed environment variables
```bash
  FLASK_SECRET_KEY=XXXX
  SQLALCHEMY_DATABASE_URI=XXXX
```
3) Setup a virtual environment:
```bash
  pip3 install virtualenv
  mkdir venv
  python3 -m virtualenv venv
```

4) Activate the virtual environment:
- On Linux and OSX
```bash
  source venv/bin/activate
```
- On Windows
```bash
  .\venv\Scripts\activate.bat
```

5) Install the dependencies:
```bash
  pip3 install -r requirements.txt
```

6) Set the FLASK_ENV and FLASK_APP environment variables:
```bash
  export FLASK_ENV=development
  export FLASK_APP=run.py
```

7) Run the development server
```bash
  flask run
```

8) you can reach the web app at: http://localhost:5000

