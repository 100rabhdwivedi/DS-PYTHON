import streamlit as st
import json
import random
import string
from datetime import datetime
from pathlib import Path

# ======================================================
# CONFIG
# ======================================================
st.set_page_config(
    page_title="Library Management System",
    page_icon="📚",
    layout="centered"
)

DATA_FILE = "library.json"

# ======================================================
# DATA LAYER
# ======================================================
class Library:
    def __init__(self):
        self.data = {"books": [], "members": []}
        self._load()

    def _load(self):
        if Path(DATA_FILE).exists():
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                if content:
                    self.data = json.loads(content)

    def save(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    @staticmethod
    def generate_id(prefix):
        return prefix + "".join(
            random.choices(string.ascii_uppercase + string.digits, k=5)
        )


lib = Library()

# ======================================================
# HELPERS
# ======================================================
def now():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def get_book(book_id):
    return next((b for b in lib.data["books"] if b["id"] == book_id), None)

def get_member(member_id):
    return next((m for m in lib.data["members"] if m["id"] == member_id), None)

# ======================================================
# UI – SIDEBAR
# ======================================================
st.title("📚 Library Management System")

menu = st.sidebar.radio(
    "📌 Menu",
    [
        "Add Book",
        "Books",
        "Add Member",
        "Members",
        "Member Details",
        "Borrow Book",
        "Return Book",
    ]
)

# ======================================================
# ADD BOOK
# ======================================================
if menu == "Add Book":
    st.subheader("➕ Add New Book")

    with st.form("add_book"):
        name = st.text_input("Book Name")
        author = st.text_input("Author Name")
        stock = st.number_input("Stock Quantity", min_value=1, step=1)
        submit = st.form_submit_button("Add Book")

    if submit:
        if not name or not author:
            st.error("All fields are required")
        else:
            lib.data["books"].append({
                "id": lib.generate_id("B"),
                "name": name,
                "author": author,
                "stock": stock,
                "available_stock": stock,
                "created_at": now()
            })
            lib.save()
            st.success("Book added successfully")

# ======================================================
# LIST BOOKS
# ======================================================
elif menu == "Books":
    st.subheader("📖 Books Inventory")

    if lib.data["books"]:
        st.dataframe(lib.data["books"], width="stretch")
    else:
        st.warning("No books available")

# ======================================================
# ADD MEMBER
# ======================================================
elif menu == "Add Member":
    st.subheader("➕ Add Member")

    with st.form("add_member"):
        name = st.text_input("Member Name")
        email = st.text_input("Email Address")
        submit = st.form_submit_button("Add Member")

    if submit:
        if not name or not email:
            st.error("All fields are required")
        else:
            lib.data["members"].append({
                "id": lib.generate_id("M"),
                "name": name,
                "email": email,
                "borrowed_books": [],
                "created_at": now()
            })
            lib.save()
            st.success("Member added successfully")

# ======================================================
# LIST MEMBERS
# ======================================================
elif menu == "Members":
    st.subheader("👥 Members List")

    if lib.data["members"]:
        st.dataframe(lib.data["members"], width="stretch")
    else:
        st.warning("No members found")

# ======================================================
# MEMBER DETAILS (PROFESSIONAL VIEW)
# ======================================================
elif menu == "Member Details":
    st.subheader("🧑‍💼 Member Details")

    if not lib.data["members"]:
        st.warning("No members found")
    else:
        member_map = {
            f"{m['name']} ({m['id']})": m["id"]
            for m in lib.data["members"]
        }

        selected = st.selectbox("Select Member", member_map)
        member = get_member(member_map[selected])

        st.markdown("### 📄 Basic Information")
        st.write("**ID:**", member["id"])
        st.write("**Name:**", member["name"])
        st.write("**Email:**", member["email"])
        st.write("**Joined On:**", member["created_at"])

        st.markdown("### 📚 Borrowed Books")

        if not member["borrowed_books"]:
            st.info("No books borrowed")
        else:
            for i, book in enumerate(member["borrowed_books"]):
                col1, col2, col3 = st.columns([4, 3, 1])
                col1.write(f"📘 {book['name']}")
                col2.write(book["borrowed_date"])

                if col3.button("Return", key=f"ret_{i}"):
                    real_book = get_book(book["id"])
                    if real_book:
                        real_book["available_stock"] += 1
                    member["borrowed_books"].remove(book)
                    lib.save()
                    st.success("Book returned")
                    st.rerun()

# ======================================================
# BORROW BOOK
# ======================================================
elif menu == "Borrow Book":
    st.subheader("📕 Borrow Book")

    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("Borrow"):
        member = get_member(member_id)
        book = get_book(book_id)

        if not member:
            st.error("Member not found")
        elif not book:
            st.error("Book not found")
        elif book["available_stock"] <= 0:
            st.warning("Book not available")
        else:
            member["borrowed_books"].append({
                "id": book_id,
                "name": book["name"],
                "borrowed_date": now()
            })
            book["available_stock"] -= 1
            lib.save()
            st.success("Book borrowed successfully")

# ======================================================
# RETURN BOOK (MANUAL)
# ======================================================
elif menu == "Return Book":
    st.subheader("📗 Return Book")

    member_id = st.text_input("Member ID")
    book_id = st.text_input("Book ID")

    if st.button("Return"):
        member = get_member(member_id)
        book = get_book(book_id)

        if not member or not book:
            st.error("Invalid Member or Book ID")
        else:
            before = len(member["borrowed_books"])
            member["borrowed_books"] = [
                b for b in member["borrowed_books"] if b["id"] != book_id
            ]

            if len(member["borrowed_books"]) == before:
                st.warning("This book was not borrowed by the member")
            else:
                book["available_stock"] += 1
                lib.save()
                st.success("Book returned successfully")

#streamlit run filename.py