from app import app, db   # where from do I load these?  whatr

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
    with app.app_context():
        db.create_all()