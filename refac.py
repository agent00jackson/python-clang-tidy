# Import the libclang python bindings
import clang.cindex
import os

# Create an index object that will parse the source file
index = clang.cindex.Index.create()

# Parse the source file and get the translation unit cursor
FILE_NAME = "test.cpp"
tu = index.parse(FILE_NAME)
cursor = tu.cursor

# Define a function that will recursively traverse the AST and replace C-style casts
def replace_casts(node):
    # Iterate over the children of the current node
    for child in node.get_children():
        # If the child is a C-style cast expression, get its source range and type
        child_file = child.location.file
        if child_file is not None and os.path.samefile(child_file.name, FILE_NAME):
            if child.kind == clang.cindex.CursorKind.CSTYLE_CAST_EXPR:
                cast_range = child.extent
                cast_type = child.type.spelling
                # Get the source code of the cast expression and its subexpression
                # by joining the spellings of the tokens in their ranges
                cast_code = "".join(t.spelling for t in tu.get_tokens(extent=cast_range))
                subexpr_code = "".join(t.spelling for t in tu.get_tokens(extent=next(child.get_children()).extent))
                # Construct a new code with static_cast instead of C-style cast
                new_code = f"static_cast<{cast_type}>({subexpr_code})"
                # Print the old and new code for comparison
                print(f"Replacing {cast_code} with {new_code}")
                # Replace the cast expression in the source file with the new code
                # You can use any method to modify the file, such as fileinput or tempfile
                # Here we just use a simple string replace for demonstration
                global source_code
                source_code = source_code.replace(cast_code, new_code)
            # Recursively traverse the child node
            replace_casts(child)

# Read the source file as a string
with open(FILE_NAME) as f:
    source_code = f.read()

# Call the replace_casts function on the root cursor
replace_casts(cursor)

# Write the modified source code to a new file
with open(f'mod_{FILE_NAME}', "w") as f:
    f.write(source_code)
