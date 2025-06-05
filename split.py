import ezdxf
import click
import os
import re

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path(file_okay=False))
@click.option('--pattern', '-p', default=None, help='Regex pattern to match layer names (optional). If omitted, all layers are exported.')
def split_by_layer_pattern(input_file, output_dir, pattern):
    """
    Splits INPUT_FILE into multiple DXF files, one per layer.
    Optionally filters layers using a regex PATTERN.
    Files are saved into OUTPUT_DIR.
    """
    doc = ezdxf.readfile(input_file)
    msp = doc.modelspace()

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Get all layers used in modelspace
    all_layers = sorted({e.dxf.layer for e in msp})

    # Filter by regex pattern, if provided
    if pattern:
        matched_layers = [name for name in all_layers if re.search(pattern, name)]
        if not matched_layers:
            click.echo(f"No layers matched pattern: '{pattern}'")
            return
        click.echo(f"Matched {len(matched_layers)} layer(s): {matched_layers}")
    else:
        matched_layers = all_layers
        click.echo(f"No pattern provided. Exporting all {len(matched_layers)} layers.")

    # Export each matched layer to a separate DXF file
    for layer in matched_layers:
        new_doc = ezdxf.new(dxfversion=doc.dxfversion)
        new_msp = new_doc.modelspace()
        for e in msp.query(f'*[layer=="{layer}"]'):
            new_msp.add_entity(e.copy())
        out_path = os.path.join(output_dir, f"{layer}.dxf")
        new_doc.saveas(out_path)
        click.echo(f"Saved layer '{layer}' to {out_path}")

if __name__ == '__main__':
    split_by_layer_pattern()

