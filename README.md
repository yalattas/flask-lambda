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

## dynamoDB
### local
In local development mode, DynamoDB will boot up a container with __no initial__ data in it.

You must have `awscli` installed on your machine and perform the following command considering changing the table name to match what you defined in environment variable `local.env`

```
aws dynamodb --endpoint-url http://localhost:8000 create-table --table-name <TABLE_NAME> \
--attribute-definitions AttributeName=attName,AttributeType=S \
--key-schema AttributeName=attName,KeyType=HASH \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

### cloud
AWS `sam` will provision a dynamoDB table, name already defined in `template.yaml` at the root of the project.

> name is set dynamically via `sam` function `!Join` that concatenate the strings together.