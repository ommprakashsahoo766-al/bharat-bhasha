# ==================================================
# LEARN PAGE
# ==================================================

elif page == "Learn":

    st.header("📖 Learn a Language")

    # Select language
    language = st.selectbox(
        "🌐 Select a language:",
        list(languages.keys()),
        key="learn_language"
    )

    topics = languages[language]
    topic_names = list(topics.keys())

    st.divider()

    # Show available topics
    st.subheader("📚 Choose a Topic")

    topic = st.selectbox(
        "Select a topic to learn:",
        topic_names,
        format_func=lambda x: f"📘 {x.replace('_', ' ').title()}",
        key="learn_topic"
    )

    # Initialize progress
    initialize_progress(language)

    completed = progress[language][topic]

    st.divider()

    # Topic heading
    st.header(
        f"📘 {topic.replace('_', ' ').title()}"
    )

    # Completion status
    if completed:
        st.success(
            "✅ You have already completed this topic!"
        )
    else:
        st.info(
            "📖 Study the words below and then mark this topic as completed."
        )

    st.divider()

    # Get vocabulary
    data = topics[topic]

    # Display vocabulary as cards
    for word, meaning in data.items():

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(
                f"### 🗣️ {word}"
            )

        with col2:
            st.markdown(
                f"### ➡️ {meaning}"
            )

        st.divider()

    # Mark completed button
    if not completed:

        if st.button(
            "✅ Mark Topic as Completed",
            key=f"complete_{language}_{topic}"
        ):

            mark_topic_completed(
                language,
                topic
            )

            st.success(
                f"🎉 {topic.replace('_', ' ').title()} "
                f"completed for {language}!"
            )

            st.rerun()

    else:

        st.success(
            "🏆 Topic Completed!"
        )


    # ==================================================
    # TOPIC PROGRESS
    # ==================================================

    st.divider()

    st.subheader("📊 Your Learning Progress")

    completed_topics = 0

    for topic_name in topic_names:

        if progress[language][topic_name]:
            completed_topics += 1

    total_topics = len(topic_names)

    topic_progress = (
        completed_topics / total_topics
    ) * 100

    st.progress(
        topic_progress / 100
    )

    st.write(
        f"**{completed_topics}/{total_topics} topics completed**"
    )

    st.write(
        f"Progress: **{topic_progress:.0f}%**"
    )
