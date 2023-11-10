from app.main import app

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as err:
        print(err)