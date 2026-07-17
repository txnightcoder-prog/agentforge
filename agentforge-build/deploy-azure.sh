#!/bin/bash
# ============================================================
# AgentForge — Azure Container Apps Deployment
# Run once to deploy. Re-run to update.
# Usage: bash deploy-azure.sh
# ============================================================
set -e

RESOURCE_GROUP="agentforge-rg"
LOCATION="eastus"
ACR_NAME="agentforgeacr"
APP_NAME="agentforge"
ENVIRONMENT_NAME="agentforge-env"
IMAGE_TAG="latest"

echo ""
echo "=================================================="
echo "  AgentForge — Azure Deployment"
echo "=================================================="

echo "[1/8] Checking Azure login..."
az account show --query "name" -o tsv || { echo "Run 'az login' first"; exit 1; }

echo "[2/8] Creating resource group: $RESOURCE_GROUP..."
az group create --name "$RESOURCE_GROUP" --location "$LOCATION" --output none

echo "[3/8] Creating Container Registry: $ACR_NAME..."
az acr create \
  --resource-group "$RESOURCE_GROUP" \
  --name "$ACR_NAME" \
  --sku Basic \
  --admin-enabled true \
  --output none

echo "[4/8] Building and pushing Docker image..."
az acr build \
  --registry "$ACR_NAME" \
  --image "${APP_NAME}:${IMAGE_TAG}" \
  .

echo "[5/8] Retrieving ACR credentials..."
ACR_USERNAME=$(az acr credential show --name "$ACR_NAME" --query "username" -o tsv)
ACR_PASSWORD=$(az acr credential show --name "$ACR_NAME" --query "passwords[0].value" -o tsv)
ACR_LOGIN_SERVER=$(az acr show --name "$ACR_NAME" --query "loginServer" -o tsv)

echo "[6/8] Creating Container Apps environment..."
az containerapp env create \
  --name "$ENVIRONMENT_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --location "$LOCATION" \
  --output none

echo "[7/8] Deploying Container App..."
az containerapp create \
  --name "$APP_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --environment "$ENVIRONMENT_NAME" \
  --image "${ACR_LOGIN_SERVER}/${APP_NAME}:${IMAGE_TAG}" \
  --registry-server "$ACR_LOGIN_SERVER" \
  --registry-username "$ACR_USERNAME" \
  --registry-password "$ACR_PASSWORD" \
  --target-port 8501 \
  --ingress external \
  --min-replicas 0 \
  --max-replicas 2 \
  --cpu 0.5 \
  --memory 1.0Gi \
  --output none

echo "[8/8] Getting live URL..."
APP_URL=$(az containerapp show \
  --name "$APP_NAME" \
  --resource-group "$RESOURCE_GROUP" \
  --query "properties.configuration.ingress.fqdn" -o tsv)

echo ""
echo "=================================================="
echo "  DEPLOYMENT COMPLETE"
echo "  Live URL: https://$APP_URL"
echo "=================================================="
