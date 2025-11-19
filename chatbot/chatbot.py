def run_chatbot(qa):
    print("\nchatbot siap digunakan! (Ketik 'exit' untuk keluar)\n")
    chat_history = []

    while True:
        query = input("You: ").strip()
        if query.lower() in ["exit", "keluar", "quit"]:
            print("\nterima kasih sudah mencoba chatbot ini!")
            break
        if not query:
            continue

        try:
            result = qa({"question": query, "chat_history": chat_history})
            answer = result["answer"]
            chat_history.append((query, answer))
            print("Bot:", answer, "\n")
        except Exception as e:
            print(f"error: {e}")
