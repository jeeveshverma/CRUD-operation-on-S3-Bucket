


{
  "log_level": "DEBUG",
  "username": "username",
  "password": "password",
  "s3_config": {
    "region": "us-east-1",
    "user_prefix": "cf",
    "policy_prefix": "cf",
    "bucket_prefix": "cf",
    "aws_partition": "aws",
    "allow_user_provision_parameters": false,
    "allow_user_update_parameters": false,
    "catalog": {
      "services": [
        {
          "id": "98FF26D0-2E01-11E5-9184-FEFF819CDC9F",
          "name": "aws-s3",
          "description": "Amazon Simple Storage Service (S3)",
          "bindable": true,
          "tags": [
            "AWS",
             "S3",
             "object-storage"
          ],
          "metadata": {
            "displayName": "Amazon Simple Storage Service (S3)",
            "imageUrl": "",
            "longDescription": "Amazon Simple Storage Service (Amazon S3), provides developers and IT teams with secure, durable, highly-scalable object storage.",
            "providerDisplayName": "Amazon Web Services",
            "documentationUrl": "https://aws.amazon.com/documentation/s3/",
            "supportUrl": "https://forums.aws.amazon.com/forum.jspa?forumID=24"
          },
          "plan_updateable": false,
          "plans": [
            {
              "id": "EAAD05D8-2E01-11E5-9184-FEFF819CDC9F",
              "name": "default",
              "description": "Provides a single S3 bucket with unlimited storage.",
              "metadata": {
                "costs": [
                  {
                    "amount": {
                      "usd": 0.0300
                    },
                    "unit": "Per GB"
                  }
                ],
                "bullets": [
                  "Single S3 bucket",
                  "Unlimited storage, unlimited number of objects."
                ]
              },
              "free": false,
              "s3_properties": {
                "iam_policy": {
                  "Version": "2012-10-17",
                  "Statement": [
                    {
                      "Action": [
                        "s3:DeleteBucketWebsite",
                        "s3:GetBucketAcl",
                        "s3:GetBucketCORS",
                        "s3:GetBucketLocation",
                        "s3:GetBucketLogging",
                        "s3:GetBucketNotification",
                        "s3:GetBucketPolicy",
                        "s3:GetBucketTagging",
                        "s3:GetBucketVersioning",
                        "s3:GetBucketWebsite",
                        "s3:ListBucket",
                        "s3:ListBucketMultipartUploads",
                        "s3:ListBucketVersions",
                        "s3:PutBucketCORS",
                        "s3:PutBucketLogging",
                        "s3:PutBucketNotification",
                        "s3:PutBucketVersioning",
                        "s3:PutBucketWebsite"
                      ],
                      "Effect": "Allow",
                      "Resource": "{{.Resource}}"
                    },
                    {
                      "Action": [
                        "s3:AbortMultipartUpload",
                        "s3:DeleteObject",
                        "s3:DeleteObjectVersion",
                        "s3:GetObject",
                        "s3:GetObjectAcl",
                        "s3:GetObjectTorrent",
                        "s3:GetObjectVersion",
                        "s3:GetObjectVersionAcl",
                        "s3:GetObjectVersionTorrent",
                        "s3:ListMultipartUploadParts",
                        "s3:PutObject",
                        "s3:PutObjectAcl",
                        "s3:PutObjectVersionAcl",
                        "s3:RestoreObject"
                      ],
                      "Effect": "Allow",
                      "Resource": "{{.Resource}}/*"
                    }
                  ]
                }
              }
            },
            {
              "id": "16A19515-C2B9-4982-80BD-69BED6A86C85",
              "name": "public",
              "description": "Provides a single publicly accessible S3 bucket with unlimited storage.",
              "metadata": {
                "costs": [
                  {
                    "amount": {
                      "usd": 0.0300
                    },
                    "unit": "Per GB"
                  }
                ],
                "bullets": [
                  "Single S3 bucket",
                  "Unlimited storage, unlimited number of objects."
                ]
              },
              "free": false,
              "s3_properties": {
                "iam_policy": {
                  "Version": "2012-10-17",
                  "Statement": [
                    {
                      "Action": [
                        "s3:DeleteBucketWebsite",
                        "s3:GetBucketAcl",
                        "s3:GetBucketCORS",
                        "s3:GetBucketLocation",
                        "s3:GetBucketLogging",
                        "s3:GetBucketNotification",
                        "s3:GetBucketPolicy",
                        "s3:GetBucketTagging",
                        "s3:GetBucketVersioning",
                        "s3:GetBucketWebsite",
                        "s3:ListBucket",
                        "s3:ListBucketMultipartUploads",
                        "s3:ListBucketVersions",
                        "s3:PutBucketCORS",
                        "s3:PutBucketLogging",
                        "s3:PutBucketNotification",
                        "s3:PutBucketVersioning",
                        "s3:PutBucketWebsite"
                      ],
                      "Effect": "Allow",
                      "Resource": "{{.Resource}}"
                    },
                    {
                      "Action": [
                        "s3:AbortMultipartUpload",
                        "s3:DeleteObject",
                        "s3:DeleteObjectVersion",
                        "s3:GetObject",
                        "s3:GetObjectAcl",
                        "s3:GetObjectTorrent",
                        "s3:GetObjectVersion",
                        "s3:GetObjectVersionAcl",
                        "s3:GetObjectVersionTorrent",
                        "s3:ListMultipartUploadParts",
                        "s3:PutObject",
                        "s3:PutObjectAcl",
                        "s3:PutObjectVersionAcl",
                        "s3:RestoreObject"
                      ],
                      "Effect": "Allow",
                      "Resource": "{{.Resource}}/*"
                    }
                  ]
                },
                "bucket_policy": {
                  "Version": "2012-10-17",
                  "Statement": [
                    {
                      "Effect": "Allow",
                      "Principal": "*",
                      "Action": ["s3:GetObject"],
                      "Resource": ["arn:{{.AwsPartition}}:s3:::{{.BucketName}}/*"]
                    }
                  ]
                }
              }
            }
          ]
        }
      ]
    }
  }
}

