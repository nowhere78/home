# AWS Retagger

A production-ready Python CLI tool that scans AWS resources across multiple named profiles for a specific tag key/value and retags them to a new key/value. Uses the **Resource Groups Tagging API** for discovery and updates.

## What It Does

AWS Retagger helps you:

- Find AWS resources across multiple profiles and regions based on existing tags
- Apply new tags to those resources
- Optionally remove old tags after applying new ones
- Perform dry runs to preview changes before applying them
- Handle large-scale retagging operations with proper batching and pagination

The tool uses AWS Resource Groups Tagging API, which provides a unified interface for tagging resources across most AWS services.

## Setup

### Prerequisites

- Python 3.11 or higher
- AWS CLI configured with appropriate profiles and credentials
- Appropriate IAM permissions for Resource Groups Tagging API operations

### Pure Virtual Environment Setup

#### macOS/Linux

```bash
# Clone or create the project directory
git clone <your-repo-url> aws-retagger
cd aws-retagger

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install the package in development mode
pip install -e .

# Verify installation
retagger --help
```

#### Windows

```cmd
# Clone or create the project directory
git clone <your-repo-url> aws-retagger
cd aws-retagger

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install the package in development mode
pip install -e .

# Verify installation
retagger --help
```

### Optional: Using Makefile (macOS/Linux)

```bash
# Set up everything with one command
make install

# Other useful targets
make format    # Format code with Black and Ruff
make lint      # Check code quality
make run ARGS="-ok Owner -ov Legacy -nk Owner -nv Platform -d"
make clean     # Remove virtual environment and build artifacts
```

## Usage Examples

### Basic Examples Using Short Flags

```bash
# Dry run across all local profiles, auto-discover regions
retagger -ok Owner -ov Legacy -nk Owner -nv Platform -d

# Specific profiles & regions
retagger -ok CostCenter -ov 1234 -nk CostCenter -nv 5678 -p dev,prod -r eu-west-1,eu-north-1

# Filter by resource types (ResourceTypeFilters)
retagger -ok Environment -ov Test -nk Environment -nv Prod -s ec2:instance,s3:bucket -d

# Keep old tag while adding new one
retagger -ok Team -ov OldTeam -nk Team -nv NewTeam -ko

# Real run with verbose logging
retagger -ok Department -ov Engineering -nk Department -nv Platform -l DEBUG
```

### Command-Line Options

| Short | Long | Required | Description |
|-------|------|----------|-------------|
| `-ok` | `--old-key` | ✓ | Existing tag key to match |
| `-ov` | `--old-value` | ✓ | Existing tag value to match |
| `-nk` | `--new-key` | ✓ | New tag key to apply |
| `-nv` | `--new-value` | ✓ | New tag value to apply |
| `-ko` | `--keep-old` | | Keep the old tag after applying the new one |
| `-r` | `--regions` | | Comma-separated regions (default: discover per profile) |
| `-p` | `--profiles` | | Comma-separated profiles (default: all local profiles) |
| `-s` | `--services` | | Comma-separated ResourceTypeFilters (e.g., `ec2:instance,s3:bucket`) |
| `-d` | `--dry-run` | | Plan only; don't call tagging APIs |
| `-m` | `--max-pages` | | Safety cap for pagination (default: 1000) |
| `-l` | `--log-level` | | Logging level: DEBUG, INFO, WARNING, ERROR (default: INFO) |

## Resource Groups Tagging API Notes and Limitations

### Service Coverage

The Resource Groups Tagging API supports most AWS services, but not all. Some notable limitations:

- Not all resource types support tagging
- Some services have their own tagging APIs with different behaviors
- New services may not be immediately supported

### Batch Operations

- Maximum 20 resource ARNs per `tag_resources` or `untag_resources` call
- The tool automatically handles batching for you

### Eventual Consistency

- Tag changes may not be immediately visible in all AWS APIs
- Allow time for propagation when verifying results

### Permissions Required

Your AWS credentials need these permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "resource-groups:GetResources",
                "tag:TagResources",
                "tag:UntagResources",
                "ec2:DescribeRegions"
            ],
            "Resource": "*"
        }
    ]
}
```

### Organization and SSO Considerations

- Cross-account access requires appropriate assume role permissions
- SSO profiles should work if properly configured with AWS CLI
- Some organization-level restrictions may apply

## Exit Codes and Logging

### Exit Codes

- `0`: Success - all operations completed without errors
- `1`: Error - one or more operations failed or were interrupted

### Logging Levels

- `ERROR`: Only critical errors that prevent operation
- `WARNING`: Non-fatal issues (e.g., permission denied for specific regions)
- `INFO`: General progress information (default)
- `DEBUG`: Detailed operation information including API calls

### Log Format

```log
2024-01-15 10:30:45 - retagger - INFO - Processing profile: production
2024-01-15 10:30:46 - retagger - INFO - Found 25 resources in us-east-1 (processed 1 pages)
2024-01-15 10:30:47 - retagger - INFO - Region us-east-1 complete: 25 tagged, 25 untagged, 0 errors
```

## Development

### Repository Setup

```bash
# Initialize new repository (if starting from scratch)
export REPO=aws-retagger
mkdir "$REPO" && cd "$REPO"
git init -b main
gh repo create "$REPO" --public --source=. --remote=origin --push
```

### Code Quality

The project uses Black and Ruff for code formatting and linting:

```bash
# Format code
make format
# or manually:
black src/
ruff --fix src/

# Check code quality
make lint
# or manually:
ruff src/
black --check src/
```

### Configuration

- Black: 100 character line length, Python 3.11+ target
- Ruff: E, F, I, UP, B rule sets enabled, ignores E501 (line length)

## Troubleshooting

### Common Issues

1. **"No profiles available"**
   - Check that AWS CLI is configured: `aws configure list-profiles`
   - Ensure credentials are valid: `aws sts get-caller-identity`

2. **"Could not discover regions"**
   - Verify EC2 permissions in your IAM policy
   - Try specifying regions manually with `-r`

3. **"No permission to list resources"**
   - Check IAM permissions for Resource Groups Tagging API
   - Some regions may have different permission requirements

4. **"Error processing batch"**
   - Some resources may not support the tagging operations
   - Check CloudTrail logs for detailed error information

### Getting Help

```bash
retagger --help
```

For issues with specific AWS services or resources, consult the AWS documentation for service-specific tagging limitations.

## License

MIT License - see LICENSE file for details.
