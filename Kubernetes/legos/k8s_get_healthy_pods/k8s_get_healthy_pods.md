{
"action_title": "Get All Kubernetes Healthy PODS in a given Namespace",
"action_description": "Get All Kubernetes Healthy PODS in a given Namespace",
"action_type": "LEGO_TYPE_K8S",
"action_entry_function": "k8s_get_healthy_pods",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_LIST",
"action_supports_iteration": true,
"action_verbs": [
"get"
],
"action_nouns": [
"kubernetes",
"pods",
"namespace"
]
}