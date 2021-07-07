import sys

## This fixes the broken volume_encryption_keys
broken_model_path = "../cloudendure/model/region.py"
fh = open(broken_model_path, mode="r")
original_file_contents = fh.readlines()
fh.close()

code_found = False
docs_found = False
with open(broken_model_path, mode="w") as wfh:
    for line in original_file_contents:
        if line == "            'volume_encryption_keys': ([str],),  # noqa: E501\n":
            print("Fixing broken code...")
            code_found = True
            wfh.write(
                "            'volume_encryption_keys': ([str,dict,none_type],),  # noqa: E501\n"
            )
        elif (
            line
            == "            volume_encryption_keys ([str]): [optional]  # noqa: E501\n"
        ):
            print("Fixing broken docs...")
            docs_found = True
            wfh.write(
                "            volume_encryption_keys ([str,dict,none_type]): [optional]  # noqa: E501\n"
            )
        else:
            wfh.write(line)

if not code_found or not docs_found:
    sys.exit(
        f"Expected line not found.  Has the swagger def changed? (code: {code_found}, docs: {docs_found})"
    )
