# from pathlib import Path

# from pipeline.kg_extraction_pipeline import (
#     KGExtractionPipeline
# )


# def main():

#     pipeline = KGExtractionPipeline()

#     input_dir = Path("data/input")

#     txt_files = sorted(
#         input_dir.glob("*.txt")
#     )

#     if not txt_files:
#         print("No input files found.")
#         return

#     total_triples = 0

#     for file_path in txt_files:

#         print("\n" + "=" * 80)
#         print(f"Processing : {file_path.name}")
#         print("=" * 80)

#         document = file_path.read_text(
#             encoding="utf-8"
#         )

#         triples = pipeline.run(
#             document
#         )

#         print("\nExtracted Triples")
#         print("-" * 80)

#         if not triples:

#             print("No triples extracted.")

#         else:

#             for triple in triples:

#                 print(triple)

#         print(f"\nTotal Triples : {len(triples)}")

#         total_triples += len(triples)

#     print("\n" + "=" * 80)
#     print("Processing Finished")
#     print("=" * 80)
#     print(f"Files Processed : {len(txt_files)}")
#     print(f"Total Triples   : {total_triples}")


# if __name__ == "__main__":
#     main()

from pathlib import Path

from pipeline.kg_extraction_pipeline import (
    KGExtractionPipeline
)


def main():

    pipeline = KGExtractionPipeline()

    input_dir = Path("data/input")

    txt_files = sorted(
        input_dir.glob("*.txt")
    )

    if not txt_files:

        print("No input files found.")
        return

    total_triples = 0

    total_files = 0

    print("\n")
    print("=" * 100)
    print("TAMIL RELATION EXTRACTION & KNOWLEDGE GRAPH PIPELINE")
    print("=" * 100)

    for file_path in txt_files:

        total_files += 1

        print("\n")
        print("=" * 100)
        print(f"Processing File : {file_path.name}")
        print("=" * 100)

        document = file_path.read_text(
            encoding="utf-8"
        )

        triples = pipeline.run(
            document
        )

        print("\n")
        print("=" * 100)
        print("FINAL NORMALIZED TRIPLES")
        print("=" * 100)

        if not triples:

            print("No triples extracted.")

        else:

            for i, triple in enumerate(
                triples,
                start=1
            ):

                print(f"{i}. {triple}")

        print("\n")
        print("-" * 100)
        print(f"Triples Extracted : {len(triples)}")
        print("-" * 100)

        total_triples += len(triples)

    print("\n")
    print("=" * 100)
    print("PIPELINE EXECUTION SUMMARY")
    print("=" * 100)

    print(f"Files Processed  : {total_files}")
    print(f"Triples Created  : {total_triples}")

    print("=" * 100)


if __name__ == "__main__":

    main()