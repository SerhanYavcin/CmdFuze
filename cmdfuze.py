import argparse
from file_management import clean_temp_files, copy_file, delete_files_with_extension, rename_files
from git_management import git_pull, git_push

def main():
    parser = argparse.ArgumentParser(description='CmdFuze: Command line tool for file management.')
    parser.add_argument('--task', type=str, required=True, help='The task to perform (clean, copy, delete, rename, git-pull, git-push)')
    
    # Diğer argümanları burada tanımlayın
    parser.add_argument('--directory', type=str, help='Directory for cleaning and file operations')
    parser.add_argument('--source', type=str, help='Source file for copying')
    parser.add_argument('--destination', type=str, help='Destination for copying')
    parser.add_argument('--extension', type=str, help='File extension for deletion')
    parser.add_argument('--old_pattern', type=str, help='Old pattern for renaming files')
    parser.add_argument('--new_pattern', type=str, help='New pattern for renaming files')
    parser.add_argument('--message', type=str, help='Commit message for git push')
    
    args = parser.parse_args()
    
    if args.task == 'clean':
        clean_temp_files(args.directory)
    elif args.task == 'copy':
        copy_file(args.source, args.destination)
    elif args.task == 'delete':
        delete_files_with_extension(args.directory, args.extension)
    elif args.task == 'rename':
        rename_files(args.directory, args.old_pattern, args.new_pattern)
    elif args.task == 'git-pull':
        git_pull(args.directory)
    elif args.task == 'git-push':
        git_push(args.directory, args.message)
    else:
        print("Unknown task. Please use 'clean', 'copy', 'delete', 'rename', 'git-pull', or 'git-push'.")

if __name__ == "__main__":
    main()
