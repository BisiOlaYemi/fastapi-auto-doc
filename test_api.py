import os
from app.core.schemas import ProjectConfig
from app.services.doc_generator import DocGenerator


project_path = os.path.abspath(os.getcwd())
print(f"Generating documentation for project: {project_path}")


config = ProjectConfig(
    project_path=project_path,
    doc_output_path="docs",
    include_private=False,
    watch_mode=False
)


doc_generator = DocGenerator(config)


result = doc_generator.document_project()


print("Documentation generated successfully!")
print(f"Total files: {result.total_files}")
print(f"Total functions: {result.total_functions}")
print(f"Total classes: {result.total_classes}")
print(f"Output path: {result.output_path}")

print("\nYou can view the documentation at:")
print(f"{os.path.join(result.output_path, 'index.html')}") 