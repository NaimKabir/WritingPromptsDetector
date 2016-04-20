# WritingPromptsDetector
Early detects soon-to-be popular writing prompts on Reddit.com

GetRedditAccessToken will get an OAuth access token for you once you've registered an app with Reddit.com.

Using the access code, you can run the WritingPromptsBot, which will trawl the top 30 posts on Reddit.com/r/WritingPrompts
and deliver hot, soon-to-be popular prompts to your phone. Parameters and thresholding may need some tuning--change at your discretion.

EVENTUALLY: This will only label posts based on statistical knowledge of what previous popular posts look like--using more features than only post velocity. Sci-Kits Learn will become a dependency at this stage.
