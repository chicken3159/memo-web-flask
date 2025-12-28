from flask import Flask, render_template, request, redirect, url_for
from service import MemoService
from storage_json import JsonMemoStorage

def create_app():
    app = Flask(__name__)

    storage = JsonMemoStorage("memo_data.json")
    service = MemoService(storage)

    @app.get("/")
    def index():
        memos = service.list_memos()
        error = request.args.get("error")
        return render_template("index.html", memos=memos, error=error)

    @app.post("/add")
    def add():
        text = request.form.get("text", "").strip()
        if not text:
            return redirect(url_for("index", error="空のメモは追加できません"))
        service.add_memo(text)
        return redirect(url_for("index"))

    @app.post("/delete/<int:memo_id>")
    def delete(memo_id: int):
        service.delete_memo(memo_id)
        return redirect(url_for("index"))

    @app.get("/edit/<int:memo_id>")
    def edit(memo_id: int):
        memos = service.list_memos()
        memo = next((m for m in memos if m.get("id") == memo_id), None)
        if memo is None:
            return "Not Found", 404
        error = request.args.get("error")
        return render_template("edit.html", memo=memo, error=error)

    @app.post("/update/<int:memo_id>")
    def update(memo_id: int):
        text = request.form.get("text", "").strip()
        if not text:
            return redirect(url_for("edit", memo_id=memo_id, error="空の内容にはできません"))
        service.update_memo(memo_id, text)
        return redirect(url_for("index"))

    return app

if __name__ == "__main__":
    app = create_app()

    if __name__ == "__main__":
        app.run(debug=True, port=5000)


