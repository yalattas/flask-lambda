# SAM application template
## Setup
In order to build up the Lambda function locally you will need to build the image
```
sam build --template template.yaml --use-container
```
Then start api in order to test it locally.
User the following
```
sam local start-api
```
> `sam local invoke` will not work as `flask` require a proxy to serve it. Then you need to user above command to test it
