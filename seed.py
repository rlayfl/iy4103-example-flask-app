from app import app, db, User, Place, Comment, Like

with app.app_context():
    u1 = User(username="alice")
    u2 = User(username="bob")
    p1 = Place(name="Colchester Castle")
    p2 = Place(name="Firstsite Art Gallery")

    db.session.add_all([u1, u2, p1, p2])
    db.session.commit()

    c1 = Comment(text="Amazing history!", user_id=u1.id, place_id=p1.id)
    c2 = Comment(text="Great exhibitions.", user_id=u2.id, place_id=p2.id)
    l1 = Like(user_id=u1.id, place_id=p1.id)
    l2 = Like(user_id=u2.id, place_id=p1.id)

    db.session.add_all([c1, c2, l1, l2])
    db.session.commit()

print("Sample data added!")
