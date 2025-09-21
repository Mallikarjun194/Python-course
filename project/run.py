from app.app import create_app

app = create_app()

if __name__ == "__main__":
    print("Flask TODO Project started running...!")
    app.run(debug=True)

