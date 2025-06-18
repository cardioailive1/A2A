# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = [ pkgs.python3 ];
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [ "ms-python.python" ];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      }; # To run something each time the workspace is (re)started, use the `onStart` hook
    };
    # Enable previews and customize configuration
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "./devserver.sh" ];
          env = { PORT = "$PORT"; };
          manager = "web";
# Your Google Cloud Project ID where Vertex AI is enabled.
    # This is essential for the Vertex AI SDK to authenticate and find resources.
    GCP_PROJECT_ID = "ai-powered-cardiology"; # <-- **REPLACE WITH YOUR PROJECT ID**

    # The Google Cloud region where your Vertex AI resources are located (e.g., "us-central1").
    # This is also needed for the SDK.
    GCP_REGION = "us-central1, us-east5,us-east4"; # <-- **REPLACE WITH YOUR REGION**

 # Default port for the application
 PORT = "8080";
        };
      };
    };
  };
}
