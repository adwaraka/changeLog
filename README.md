changelog Tool

This was the initial design and thought-process for a tool that can take the commits for the past N days and generate a changelog based on the data. No repos were harmed during the making - as I am using my own repos for testing. The project requires a user to set and utilize a GIT Access token.

![earlyDesign](earlyDesign.png)

Due to restrictions, the current implementation was only able to achieve the following. I have marked the ones that are pending in the following.

![implementation](implementation.png)

I have also utilized a simple summarization algorithm using weighted frequency and sentence-scoring to only extract commit messages of relevance. This would prove helpful if the developers tend to write rather verbose commit messages (based on my experience at work).

Please find the usage in the changelog.mp4 video folder. Note that the user facing app will be in my other repository which is https://github.com/adwaraka/my-app/tree/feature/change-log-app.
