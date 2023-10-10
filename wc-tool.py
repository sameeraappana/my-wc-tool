#!/usr/bin/env python3
import click
import sys

@click.command()
@click.option("--name", prompt="Enter your name", help="Name of the user")
def hello(name):
    click.echo(f"Helloooooooo {name}!")

@click.command()
@click.argument('input_file', type=click.Path(exists=True), required=False)
@click.option('-w', '--count-words', is_flag=True, help='count of words in a text file')
@click.option('-b', '--count-bytes', is_flag=True, help='count of bytes in a text file')
@click.option('-l', '--count-lines', is_flag=True, help='count of lines in a text file')
@click.option('-c', '--count-characters', is_flag=True, help='count of characters in a text file')
def get_count(input_file, count_words, count_bytes, count_lines, count_characters):
    try:
        if input_file:
            with open(input_file, 'rb') as file:
                text = file.read()
        else:
            text =  sys.stdin.read().encode()

        if count_words:
            result = word_count(text)
        elif count_bytes:
            result = byte_count(text)
        elif count_lines:
            result = line_count(text) 
        elif count_characters:
            result = char_count(text)  
        else:
            click.echo(f"word count: {word_count(text)} byte count: {byte_count(text)} line count: {line_count(text)} {input_file}")
            sys.exit()
        click.echo(f"{result} {input_file}")
    except Exception as e:
        click.echo("error occurred")

def word_count(text):
    return len(text.split())
def byte_count(text):
    return len(text)
def line_count(text):
    return len(text.splitlines())
def char_count(text):
    return len(text.decode())

if __name__ == "__main__":
    get_count()