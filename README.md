#activate the .venv
\Users\'your_user'\\'folder_name'\\.venv\Scripts\activate.bat


#Activate Dockerfile

docker build -t auth-api:latest .

docker run --rm -p 5000:5000 --env FLASK_ENV=development auth-api:latest
