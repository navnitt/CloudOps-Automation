{
"action_title": "Delete AWS Default Encryption for S3 Bucket",
"action_description": "Delete AWS Default Encryption for S3 Bucket",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_delete_bucket_encryption",
"action_needs_credential": true,
"action_output_type": "ACTION_OUTPUT_TYPE_DICT",
"action_supports_poll": true,
"action_supports_iteration": true,
"action_verbs": [
"delete"
],
"action_nouns": [
"aws",
"s3",
"encryption"
]
}