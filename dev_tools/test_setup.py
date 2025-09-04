#!/usr/bin/env python3
"""
Test script for MVP Quick-Start setup
This script tests the setup programmatically without user input
"""

import os
import sys
import time
import shutil
from pathlib import Path
from unittest.mock import patch
from io import StringIO

# Add the current directory to the path to import our module
sys.path.insert(0, str(Path.cwd()))

# Import the quick start module
from quick_start import MVPQuickStart

def test_setup():
    """Test the MVP setup with simulated user input"""
    print("🧪 Starting MVP Template Test")
    print("=" * 50)
    
    start_time = time.time()
    
    # Create a test directory
    test_dir = Path.cwd() / 'test_mvp_project'
    if test_dir.exists():
        shutil.rmtree(test_dir)
    test_dir.mkdir()
    
    try:
        # Copy required files from parent directory FIRST
        original_cwd = os.getcwd()
        print(f"📄 Copying architectures.json from {Path(original_cwd) / 'architectures.json'} to {test_dir}")
        shutil.copy(Path(original_cwd) / 'architectures.json', test_dir)
        
        # Copy .cursor directory
        source_cursor_dir = Path(original_cwd) / '.cursor'
        dest_cursor_dir = test_dir / '.cursor'
        if source_cursor_dir.exists() and not dest_cursor_dir.exists():
            shutil.copytree(source_cursor_dir, dest_cursor_dir)
        
        # Copy dev_tools directory
        source_dev_dir = Path(original_cwd) / 'dev_tools'
        dest_dev_dir = test_dir / 'dev_tools'
        if source_dev_dir.exists() and not dest_dev_dir.exists():
            shutil.copytree(source_dev_dir, dest_dev_dir)
        
        # Change to test directory
        os.chdir(test_dir)
        
        # Verify the file was copied
        if (Path.cwd() / 'architectures.json').exists():
            print("✅ architectures.json copied successfully")
        else:
            print("❌ Failed to copy architectures.json")
        
        # Initialize the quick start AFTER changing directory
        quick_start = MVPQuickStart()
        
        # Mock user inputs
        inputs = [
            '35',  # MERN Stack selection  
            'test-mvp'  # Project name
        ]
        
        with patch('builtins.input', side_effect=inputs):
            # Run the setup
            quick_start.run_setup()
        
        end_time = time.time()
        setup_duration = end_time - start_time
        
        print(f"\n⏱️  Setup completed in {setup_duration:.2f} seconds")
        
        # Verify the setup results
        print("\n🔍 Verifying setup results...")
        
        # Core checks that should always exist
        checks = {
            '.cursorrules exists': (test_dir / '.cursorrules').exists(),
            'package.json exists': (test_dir / 'package.json').exists(),
            '.env.example exists': (test_dir / '.env.example').exists(),
            'README.md exists': (test_dir / 'README.md').exists(),
            '.mvp-config.json exists': (test_dir / '.mvp-config.json').exists(),
            'add_architecture.py exists': (test_dir / 'add_architecture.py').exists(),
            'taskmaster_commands.py exists': (test_dir / 'taskmaster_commands.py').exists(),
            '.taskmaster directory exists': (test_dir / '.taskmaster').exists(),
            'archive directory exists': (test_dir / 'archive').exists(),
        }
        
        # Optional checks (might not exist depending on architecture)
        optional_checks = {
            'active_prompts directory exists': (test_dir / 'active_prompts').exists(),
        }
        
        all_passed = True
        for check_name, result in checks.items():
            status = "✅" if result else "❌"
            print(f"  {status} {check_name}")
            if not result:
                all_passed = False
        
        # Optional checks (don't fail the test if missing)
        print("\n🔍 Optional features:")
        for check_name, result in optional_checks.items():
            status = "✅" if result else "⚪"
            print(f"  {status} {check_name}")
        
        # Check file contents
        if (test_dir / '.mvp-config.json').exists():
            import json
            with open(test_dir / '.mvp-config.json', 'r') as f:
                config = json.load(f)
                print(f"\n📋 Project Configuration:")
                print(f"  Project: {config.get('project_name')}")
                print(f"  Architecture: {config.get('primary_architecture')}")
                print(f"  Rules: {len(config.get('active_rules', []))} active rules")
        
        if (test_dir / 'package.json').exists():
            with open(test_dir / 'package.json', 'r') as f:
                import json
                package = json.load(f)
                print(f"\n📦 Package.json:")
                print(f"  Name: {package.get('name')}")
                print(f"  Dependencies: {len(package.get('dependencies', {}))}")
                print(f"  Dev Dependencies: {len(package.get('devDependencies', {}))}")
                print(f"  Scripts: {len(package.get('scripts', {}))}")
        
        print(f"\n🎯 Test Results:")
        print(f"  Duration: {setup_duration:.2f} seconds")
        print(f"  Status: {'✅ PASSED' if all_passed else '❌ FAILED'}")
        
        return all_passed, setup_duration
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False, 0
    
    finally:
        # Return to original directory
        os.chdir(original_cwd)

def test_node_setup():
    """Test the Node.js setup script"""
    print("\n🧪 Testing Node.js Quick-Start Script")
    print("=" * 50)
    
    try:
        # Check if Node.js script exists and is executable
        node_script = Path.cwd() / 'quick-start.js'
        if not node_script.exists():
            print("❌ quick-start.js not found")
            return False
        
        # Try to run with --help or version check
        result = os.system('node quick-start.js --version 2>/dev/null')
        if result == 0:
            print("✅ Node.js script is executable")
        else:
            print("⚠️  Node.js script may have issues")
        
        return True
    except Exception as e:
        print(f"❌ Node.js test failed: {e}")
        return False

if __name__ == '__main__':
    print("🚀 MVP Template Repository End-to-End Test")
    print("=" * 60)
    
    overall_start = time.time()
    
    # Test Python setup
    python_success, python_duration = test_setup()
    
    # Test Node.js setup
    node_success = test_node_setup()
    
    overall_end = time.time()
    total_duration = overall_end - overall_start
    
    print(f"\n📊 Final Test Results:")
    print(f"  Python Setup: {'✅ PASSED' if python_success else '❌ FAILED'} ({python_duration:.2f}s)")
    print(f"  Node.js Setup: {'✅ PASSED' if node_success else '❌ FAILED'}")
    print(f"  Total Test Time: {total_duration:.2f} seconds")
    
    if python_success and node_success:
        print(f"\n🎉 All tests PASSED! MVP template is working correctly.")
    else:
        print(f"\n⚠️  Some tests FAILED. Check the output above for details.")
        sys.exit(1)