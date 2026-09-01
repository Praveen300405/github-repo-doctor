import streamlit as st

from github_api import get_repository, get_files, get_commits
from analyzer import analyze_repository
from scoring import calculate_score, get_status


# Page configuration
st.set_page_config(
    page_title="GitHub Repo Doctor",
    page_icon="🚑",
    layout="wide"
)


# Title
st.title("🚑 GitHub Repo Doctor")
st.write("Analyze a public GitHub repository and check its development quality.")


# Input
repo_url = st.text_input(
    "🔗 Enter a public GitHub repository URL",
    placeholder="https://github.com/username/project"
)


# Analyze button
if st.button("🔍 Analyze Repository"):

    if not repo_url:
        st.warning("Please enter a GitHub repository URL.")

    else:

        with st.spinner("Analyzing repository..."):

            repository = get_repository(repo_url)

            if repository is None:

                st.error("Repository not found. Please check the URL.")

            else:

                owner = repository["owner"]["login"]
                repo = repository["name"]

                files = get_files(owner, repo)
                commits = get_commits(owner, repo)

                analysis = analyze_repository(
                    files,
                    commits
                )

                score = calculate_score(analysis)
                status = get_status(score)

                st.success("Repository analyzed successfully! 🎉")

                st.divider()

                # Repository overview
                st.subheader("📊 Repository Overview")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "⭐ Stars",
                        repository["stargazers_count"]
                    )

                with col2:
                    st.metric(
                        "🍴 Forks",
                        repository["forks_count"]
                    )

                with col3:
                    st.metric(
                        "🐛 Open Issues",
                        repository["open_issues_count"]
                    )

                with col4:
                    st.metric(
                        "👀 Watchers",
                        repository["watchers_count"]
                    )

                st.divider()

                # Health score
                st.subheader("❤️ Repository Health")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Health Score",
                        f"{score}/100"
                    )

                with col2:
                    st.metric(
                        "Status",
                        status
                    )

                st.progress(score / 100)

                st.divider()

                # Quality checks
                st.subheader("🔎 Quality Checks")

                col1, col2, col3 = st.columns(3)

                with col1:

                    if analysis["readme"]:
                        st.success("✅ README.md")
                    else:
                        st.error("❌ README.md")

                    if analysis["gitignore"]:
                        st.success("✅ .gitignore")
                    else:
                        st.error("❌ .gitignore")

                with col2:

                    if analysis["requirements"]:
                        st.success("✅ requirements.txt")
                    else:
                        st.error("❌ requirements.txt")

                    if analysis["tests"]:
                        st.success("✅ Tests")
                    else:
                        st.error("❌ Tests")

                with col3:

                    if analysis["commits"]:
                        st.success("✅ Git Commits")
                    else:
                        st.error("❌ Git Commits")

                st.divider()

                # Recommendations
                st.subheader("💡 Recommendations")

                recommendations = []

                if not analysis["readme"]:
                    recommendations.append(
                        "Add a README.md file."
                    )

                if not analysis["gitignore"]:
                    recommendations.append(
                        "Add a .gitignore file."
                    )

                if not analysis["requirements"]:
                    recommendations.append(
                        "Add a requirements.txt file."
                    )

                if not analysis["tests"]:
                    recommendations.append(
                        "Add automated tests."
                    )

                if not recommendations:

                    st.success(
                        "🎉 Great job! No major improvements detected."
                    )

                else:

                    for recommendation in recommendations:
                        st.write(
                            f"• {recommendation}"
                        )