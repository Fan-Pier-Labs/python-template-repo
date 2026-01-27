#!/usr/bin/env python3
"""Deploy script wrapper"""
import sys
import os
from pathlib import Path

def main():
    # Get deploy.yaml path from command line args or use default
    deploy_file = sys.argv[1] if len(sys.argv) > 1 else 'deploy.yaml'
    
    try:
        # Try to find and run the deploy package
        import importlib.util
        spec = importlib.util.find_spec('deploy')
        
        if spec is None:
            print("Error: deploy package not found. Install it with: pip install -r requirements.txt")
            sys.exit(1)
        
        # Get the deploy package location
        if spec.submodule_search_locations:
            deploy_path = spec.submodule_search_locations[0]
            main_py = Path(deploy_path) / 'main.py'
            
            if main_py.exists():
                # Set sys.argv to match expected format
                sys.argv = ['deploy', deploy_file]
                # Execute the deploy main.py
                with open(main_py, 'r') as f:
                    exec(compile(f.read(), str(main_py), 'exec'), {'__name__': '__main__', '__file__': str(main_py)})
            else:
                print(f"Error: Could not find deploy/main.py at {main_py}")
                sys.exit(1)
        else:
            print("Error: Could not locate deploy package")
            sys.exit(1)
    except SystemExit:
        raise
    except Exception as e:
        print(f"Error running deploy: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
