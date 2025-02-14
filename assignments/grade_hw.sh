
#!/bin/bash

# Check if directory argument is provided
if [ $# -eq 0 ]; then
    echo "No assignment directory specified"
    echo "Usage: $0 <assignment_directory>"
    exit 1
fi

# Run grade.sh in the specified directory
cd "$1" && ./grade.sh
