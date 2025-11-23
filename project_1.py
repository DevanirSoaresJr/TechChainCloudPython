"""
TechChainCloudPython - Project 1
A foundational CLI app demonstrating Python basics.
"""

import argparse
import sys

def main():
    """
    Main entry point for the CLI application.
    """
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="TechChainCloudPython CLI - A tool to demonstrate Python fundamentals."
    )

    # Add arguments
    parser.add_argument(
        "--name",
        type=str,
        help="Your name to greet.",
        default="Cloud Engineer"
    )

    parser.add_argument(
        "--echo",
        type=str,
        help="A message to echo back."
    )

    # Parse arguments
    args = parser.parse_args()

    # Demonstration of f-strings and basic logic
    print(f"👋 Hello, {args.name}! Welcome to TechChainCloudPython.")

    if args.echo:
        print(f"📢 Echoing your message: '{args.echo}'")
        print(f"   (Uppercase version: {args.echo.upper()})")

    print("\n✅ System Status: Active")
    print(f"🐍 Python Version: {sys.version.split()[0]}")

if __name__ == "__main__":
    main()
