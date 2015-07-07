#!/bin/bash

tmpfile=$( mktemp )

cat > $tmpfile << EOF
{
	"ID": "vault:`uname -n`",
	"Name": "vault",
	"Port": 8200,
	"Check": {
		"Script": "/usr/local/bin/vault-health-check.sh",
		"Interval": "15s"
	}
}
EOF

curl -X PUT http://localhost:8500/v1/agent/service/register -d @$tmpfile

rm -f $tmpfile
