def generate(text:str) -> str:
    if not text:
        raise ValueError('Avatar SVG Generate: name must not be empty')

    names = text.upper().split()
    first_initial = names[0][0]
    last_initial = names[-1][0]
    initials = first_initial + last_initial if len(names) > 1 else first_initial

    svg = f"""
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="48"
    height="48"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    stroke-width="0.7"
    stroke-linecap="round"
    stroke-linejoin="round"
    class="group-hover:stroke-zinc-500 dark:stroke-white group-hover:dark:stroke-zinc-500 transition-colors duration-300 ease-in-out">
    <circle cx="12" cy="12" r="10"></circle>
    <style>
        text {{
        font-family: 'Inter', sans-serif;
        font-weight: 10;
        font-size: 8px;
        }}
    </style>
    <text 
        text-anchor="middle" 
        y="50%" x="50%" dy="0.35em" 
        pointer-events="auto">
        {initials}
    </text>
</svg> 
"""
    
    return svg

def main() -> None:
    # Example usage
    example_name = "first second last"
    print(generate(example_name))

if __name__ == '__main__':
    main()