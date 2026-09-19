import codecs


def chunked_file_reader(file_path, chunk_size_bytes=1024 * 1024,
                        encoding="utf-8"):
    """Lazily yield complete lines, reading the file in fixed-size chunks.

    Args:
        file_path:        path to the text file.
        chunk_size_bytes: number of bytes read per block (default 1 MB).
        encoding:         text encoding of the file.

    Yields:
        One complete line at a time (with its trailing newline), even when
        the line spans two or more chunks.

    Peak memory is about chunk_size_bytes plus the longest line.
    """
    # incremental decoder: safe when a multi-byte character is split
    decoder = codecs.getincrementaldecoder(encoding)()
    leftover = ""            # partial line carried to the next chunk

    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(chunk_size_bytes)   # read ONE block only
            if not chunk:                      # end of file
                break

            text = leftover + decoder.decode(chunk)
            lines = text.split("\n")
            leftover = lines.pop()             # last piece may be incomplete

            for line in lines:                 # all others are complete
                yield line + "\n"

        leftover += decoder.decode(b"", final=True)  # flush buffered bytes

    if leftover:                       # final line with no newline
        yield leftover


# Example: using it in a pipeline with the csv module
import csv

def count_rows_for_town(path, town, town_column=2):
    reader = csv.reader(chunked_file_reader(path, 1024 * 1024))
    next(reader)                                   # skip the header row
    return sum(1 for row in reader if row[town_column] == town)

# print(count_rows_for_town("learners_50gb.csv", "Harare"))