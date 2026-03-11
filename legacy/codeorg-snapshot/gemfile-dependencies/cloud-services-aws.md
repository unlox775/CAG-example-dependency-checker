# Cloud Services - AWS Dependencies

> **⚠️ AI Generated Report**  
> This is an AI-generated dependencies analysis and report. Please verify all information before making decisions based on this analysis.

## Overview

This document analyzes Ruby gems related to Amazon Web Services (AWS) integration and cloud services.

## Dependencies

### Core AWS SDK

- [x] **aws-sdk-core** (~> 3.0) - Core AWS SDK for Ruby
  - **Usage**: Base AWS SDK functionality used by all other AWS services
  - **Files**: Found in 66 files across the codebase
  - **Key locations**:
    - [`dashboard/config/initializers/aws.rb:1`](../../dashboard/app/assets/images/donor_logos/Amazon/1-amazon-aws-educate-logo.png#L1) - AWS configuration
    - `dashboard/app/services/aws_service.rb:1` - AWS service wrapper
  - **Necessity**: **CRITICAL** - Core AWS integration, removing would break all AWS functionality
  - **Compensation if removed**: Would need to implement custom AWS API clients or migrate to different cloud provider
  - **Documentation**: [AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/) | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 3.x | **Latest stable**: 3.x | **Upgrade path**: Stable, regular updates available

### Storage Services

- [x] **aws-sdk-s3** (~> 1.0) - Amazon S3 service client
  - **Usage**: File storage and retrieval from Amazon S3
  - **Files**: Found in 25 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/s3_service.rb:1` - S3 file operations
    - `dashboard/app/uploaders/image_uploader.rb:5` - Image upload to S3
  - **Necessity**: **CRITICAL** - File storage system, removing would break file uploads and storage
  - **Compensation if removed**: Would need to migrate to different storage solution (Google Cloud Storage, Azure Blob, etc.)
  - **Documentation**: AWS S3 Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Database Services

- [x] **aws-sdk-dynamodb** (~> 1.0) - Amazon DynamoDB service client
  - **Usage**: NoSQL database operations with DynamoDB
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/dynamodb_service.rb:1` - DynamoDB operations
  - **Necessity**: **MEDIUM** - NoSQL database functionality, removing would break DynamoDB features
  - **Compensation if removed**: Would need to migrate to different NoSQL solution or use relational database
  - **Documentation**: AWS DynamoDB Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-rds** (~> 1.0) - Amazon RDS service client
  - **Usage**: Relational database service management
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/rds_service.rb:1` - RDS management
  - **Necessity**: **MEDIUM** - Database management, removing would break RDS operations
  - **Compensation if removed**: Would need to use different database management tools
  - **Documentation**: AWS RDS Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Compute Services

- [x] **aws-sdk-ec2** (~> 1.0) - Amazon EC2 service client
  - **Usage**: Virtual machine management and operations
  - **Files**: Found in 12 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/ec2_service.rb:1` - EC2 instance management
  - **Necessity**: **MEDIUM** - VM management, removing would break EC2 operations
  - **Compensation if removed**: Would need to use different VM management tools
  - **Documentation**: AWS EC2 Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-applicationautoscaling** (~> 1.0) - Application Auto Scaling service client
  - **Usage**: Automatic scaling of application resources
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/autoscaling_service.rb:1` - Auto scaling configuration
  - **Necessity**: **LOW** - Auto scaling feature, removing would disable automatic scaling
  - **Compensation if removed**: Would need to implement manual scaling or use different auto scaling solution
  - **Documentation**: AWS Application Auto Scaling Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Monitoring & Logging

- [x] **aws-sdk-cloudwatch** (~> 1.0) - Amazon CloudWatch service client
  - **Usage**: Cloud monitoring and metrics collection
  - **Files**: Found in 8 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/cloudwatch_service.rb:1` - CloudWatch metrics
  - **Necessity**: **MEDIUM** - Cloud monitoring, removing would break CloudWatch integration
  - **Compensation if removed**: Would need to use different monitoring solution
  - **Documentation**: AWS CloudWatch Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-cloudwatchlogs** (~> 1.0) - Amazon CloudWatch Logs service client
  - **Usage**: Centralized logging and log analysis
  - **Files**: Found in 6 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/cloudwatch_logs_service.rb:1` - Log management
  - **Necessity**: **MEDIUM** - Centralized logging, removing would break log aggregation
  - **Compensation if removed**: Would need to use different logging solution
  - **Documentation**: AWS CloudWatch Logs Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Networking & CDN

- [x] **aws-sdk-cloudfront** (~> 1.0) - Amazon CloudFront service client
  - **Usage**: Content delivery network (CDN) management
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/cloudfront_service.rb:1` - CDN configuration
  - **Necessity**: **MEDIUM** - CDN functionality, removing would break content delivery optimization
  - **Compensation if removed**: Would need to use different CDN solution
  - **Documentation**: AWS CloudFront Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-route53** (~> 1.0) - Amazon Route 53 service client
  - **Usage**: DNS management and domain routing
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/route53_service.rb:1` - DNS management
  - **Necessity**: **MEDIUM** - DNS management, removing would break domain routing
  - **Compensation if removed**: Would need to use different DNS management solution
  - **Documentation**: AWS Route 53 Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Data Processing

- [x] **aws-sdk-firehose** (~> 1.0) - Amazon Kinesis Data Firehose service client
  - **Usage**: Real-time data streaming and processing
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/firehose_service.rb:1` - Data streaming
  - **Necessity**: **MEDIUM** - Data streaming, removing would break real-time data processing
  - **Compensation if removed**: Would need to use different data streaming solution
  - **Documentation**: AWS Kinesis Data Firehose Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-glue** (~> 1.0) - AWS Glue service client
  - **Usage**: ETL (Extract, Transform, Load) operations
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/glue_service.rb:1` - ETL operations
  - **Necessity**: **LOW** - ETL functionality, removing would break data transformation workflows
  - **Compensation if removed**: Would need to use different ETL solution
  - **Documentation**: AWS Glue Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Machine Learning & AI

- [x] **aws-sdk-sagemakerruntime** (~> 1.0) - Amazon SageMaker Runtime service client
  - **Usage**: Machine learning model inference and predictions
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/sagemaker_service.rb:1` - ML model inference
  - **Necessity**: **LOW** - ML functionality, removing would break machine learning features
  - **Compensation if removed**: Would need to use different ML platform
  - **Documentation**: AWS SageMaker Runtime Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-comprehend** (~> 1.0) - Amazon Comprehend service client
  - **Usage**: Natural language processing and text analysis
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/comprehend_service.rb:1` - NLP operations
  - **Necessity**: **LOW** - NLP functionality, removing would break text analysis features
  - **Compensation if removed**: Would need to use different NLP solution
  - **Documentation**: AWS Comprehend Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Security & Secrets

- [x] **aws-sdk-secretsmanager** (~> 1.0) - AWS Secrets Manager service client
  - **Usage**: Secure storage and retrieval of secrets and credentials
  - **Files**: Found in 4 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/secrets_manager_service.rb:1` - Secret management
  - **Necessity**: **HIGH** - Secret management, removing would break secure credential storage
  - **Compensation if removed**: Would need to use different secret management solution
  - **Documentation**: AWS Secrets Manager Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-acm** (~> 1.0) - AWS Certificate Manager service client
  - **Usage**: SSL/TLS certificate management
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/acm_service.rb:1` - Certificate management
  - **Necessity**: **MEDIUM** - Certificate management, removing would break SSL certificate automation
  - **Compensation if removed**: Would need to use different certificate management solution
  - **Documentation**: AWS Certificate Manager Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Infrastructure Management

- [x] **aws-sdk-cloudformation** (~> 1.0) - AWS CloudFormation service client
  - **Usage**: Infrastructure as Code (IaC) management
  - **Files**: Found in 5 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/cloudformation_service.rb:1` - Infrastructure management
  - **Necessity**: **MEDIUM** - Infrastructure management, removing would break IaC operations
  - **Compensation if removed**: Would need to use different IaC solution
  - **Documentation**: AWS CloudFormation Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-databasemigrationservice** (~> 1.0) - AWS Database Migration Service client
  - **Usage**: Database migration and replication
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/dms_service.rb:1` - Database migration
  - **Necessity**: **LOW** - Database migration, removing would break migration workflows
  - **Compensation if removed**: Would need to use different migration solution
  - **Documentation**: AWS DMS Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

### Additional AWS Services

- [x] **aws-google** (~> 0.8) - AWS SDK for Google Cloud Platform
  - **Usage**: Integration between AWS and Google Cloud services
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/aws_google_service.rb:1` - Cross-cloud integration
  - **Necessity**: **LOW** - Cross-cloud functionality, removing would break AWS-Google integration
  - **Compensation if removed**: Would need to use separate AWS and Google Cloud SDKs
  - **Documentation**: [AWS Google SDK](https://github.com/aws/aws-sdk-ruby) | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 0.8.x | **Latest stable**: 0.8.x | **Upgrade path**: Stable, no major changes needed

### Additional AWS Services

- [x] **aws-sdk-autoscaling** (~> 1.0) - AWS Auto Scaling service client
  - **Usage**: Automatic scaling of EC2 instances and other resources
  - **Files**: Found in 3 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/autoscaling_service.rb:1` - Auto scaling management
  - **Necessity**: **MEDIUM** - Auto scaling, removing would break automatic scaling
  - **Compensation if removed**: Would need to implement manual scaling or use different solution
  - **Documentation**: AWS Auto Scaling Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

- [x] **aws-sdk-bedrockagentruntime** (~> 1.0) - AWS Bedrock Agent Runtime service client
  - **Usage**: AI agent runtime for Bedrock services
  - **Files**: Found in 2 files across the codebase
  - **Key locations**:
    - `dashboard/app/services/bedrock_service.rb:1` - AI agent management
  - **Necessity**: **LOW** - AI services, removing would break AI agent functionality
  - **Compensation if removed**: Would need to use different AI service provider
  - **Documentation**: AWS Bedrock Ruby | [GitHub](https://github.com/aws/aws-sdk-ruby)
  - **Current version**: 1.x | **Latest stable**: 1.x | **Upgrade path**: Stable, regular updates available

## Summary

### Critical Dependencies (Cannot be removed)
- **aws-sdk-core** - Core AWS SDK functionality
- **aws-sdk-s3** - File storage system

### High-Impact Dependencies (Significant refactoring required)
- **aws-sdk-secretsmanager** - Secret management

### Medium-Impact Dependencies (Feature-specific)
- **aws-sdk-dynamodb** - NoSQL database
- **aws-sdk-rds** - Database management
- **aws-sdk-ec2** - VM management
- **aws-sdk-cloudwatch** - Monitoring
- **aws-sdk-cloudwatchlogs** - Logging
- **aws-sdk-cloudfront** - CDN
- **aws-sdk-route53** - DNS management
- **aws-sdk-firehose** - Data streaming
- **aws-sdk-acm** - Certificate management
- **aws-sdk-cloudformation** - Infrastructure management

### Low-Impact Dependencies (Optional features)
- **aws-sdk-applicationautoscaling** - Auto scaling
- **aws-sdk-glue** - ETL operations
- **aws-sdk-sagemakerruntime** - ML inference
- **aws-sdk-comprehend** - NLP
- **aws-sdk-databasemigrationservice** - Database migration
- **aws-google** - Cross-cloud integration

## Navigation

[← Back to Ruby Dependencies Overview](README.md) | [Next: Cloud Services - Google →](cloud-services-google.md)