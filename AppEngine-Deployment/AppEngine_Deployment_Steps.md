To be able to deploy the codebase on AppEngine you need to first sign into your GCP account or create one if you don't have one! You'll also want to set up a billing account you can connect your project to in order to build your app.*

* Copy your repo into your Cloud Shell VM
    * Either edit and use the button in the GitHub README OR 
    * Go to the Cloud Shell (https://console.cloud.google.com/cloudshell/editor) and clone it yourself: git clone [GITHUB-URL]
    * Move into the repo by running `cd [NAME-OF-REPO]` in the black console at the bottom of the screen, which is where you'll run all the commands from here on out. (You'll need to replace [NAME-OF-REPO] with your actual repo.)
* Launch your app locally (helpful for testing)
    * Use this command to test deploy your app: 
        `dev_appserver.py ./app.yaml`
    * Once you see output like: "Booting worker with pid" in the command line, you can see your app by hitting the button that looks like <> in a browser window at the top right hand side of your screen. This will open a new tab running your app. If you haven't put anything at the "\" end point, this will just a 404. 
    * Use `CTRL + C` to close your app
* Create a project & enable billing.
    * Run these commands, replacing [YOUR-PROJECT-ID] with your actual product ID. 
        * `gcloud projects create [YOUR-PROJECT-ID]`
        * `gcloud config set project [YOUR-PROJECT-ID]`
    * You'll see your project id in yellow
    * Enable cloud build by going to this URL & clicking "enable", then following the prompts: https://console.developers.google.com/apis/library/cloudbuild.googleapis.com. 
* Launch the app!
    * Deploy your app by running this command:
        * `gcloud app deploy ./index.yaml ./app.yaml`
    * Pick a region (I'd recommend one closer to you to reduce latency)
    * Enter "y" when asked whether you want to continue
    * After it's finished deploying, your app will be at the URL: https://[YOUR-PROJECT-ID].appspot.com/

    You can consume the API endpoint using https://[YOUR-PROJECT-ID].appspot.com/[YOUR-ENDPOINT-NAME] via any REST client/cURL.

Following is a snap of the message you get if the deployment was successful:
![](https://i.ibb.co/2c1WXsD/Screenshot-from-2019-07-28-22-18-15.png)