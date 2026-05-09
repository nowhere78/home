# Infrastructure

Infrastructure-as-Code for the WidgetAI platform.

## Structure

```
infra/
├── terraform/    # Cloud resource provisioning (EKS, RDS, DynamoDB, ElastiCache, CloudFront)
├── k8s/          # Raw Kubernetes manifests (namespaces, RBAC, network policies)
└── helm/         # Helm charts for each service
```

## Prerequisites

- Terraform 1.5+
- `kubectl` configured for your cluster
- Helm 3.12+
- AWS CLI v2

## Environments

| Environment | Terraform Workspace | Notes |
|-------------|--------------------|-|
| `dev` | `dev` | Shared cluster, namespace-isolated |
| `staging` | `staging` | Isolated cluster, production-equivalent |
| `production` | `production` | Multi-AZ, autoscaling, full observability |

## Provisioning

```bash
cd infra/terraform
terraform workspace select production
terraform plan -out=tfplan
terraform apply tfplan
```

## Deployment

```bash
# Deploy a service using Helm
helm upgrade --install api-gateway ./helm/api-gateway \
  --namespace widgetai \
  --values ./helm/api-gateway/values-production.yaml
```

See [ADR-005](../adr/ADR-005-deployment-infrastructure.md) for deployment strategy details.
