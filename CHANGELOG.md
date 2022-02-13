
## [unreleased]
### Added
- More Unit tests
- Add argument (return_df) to the build function to return the pandas dataframe
- Add argument (export_csv) to the build function to write the dataset as a CSV file
- Add argument (output_path) a directory path for building datasets in
- Add DataType: random_float to generate random floats

### Changed
- Fixed a bug in data type: Decrement, where it was adding extra row

## [0.0.6] - 2022-02-01
### Added
- Unit Tests
- DataSet now accepts a path to any custom JSON schema
- CICD Support

### Changed
- Rename the mocker class to factory
- reduce amount of dataset class properties (size,task) and add them to a hashmap object
- Rename Schema_location to Schema_path
- Raise exceptions with invalid JSON schema files


## [0.0.5] - 2022-01-07
### Changed
- Simplify logic: Processing one task a time
- Simplify logic: Cleaner columns data types logic
- Simplify logic: Clean up the house and remove the useless functions and logic


## [0.0.4] - 2021-11-13
### Added
- Functions headers and documentation
- Introduce the Modifier: Between to support complex column data types
- Version tracking file
- Student schema
### Changed
- Arrange Mocker generators functions alphabetically | Mocker Class
- Naming conventions | Mocker Class
- Documentation
### Removed
- Schema yaml, As I migrated the package to use JSON | Schema

## [0.0.3] - 2021-11-05
### Changed
- Support schema files in JSON instead of YAML, As JSON is a native python lib, and I faced multiple problems on different machines with yaml

## [0.0.2] - 2021-11-05
### Added
- First proof of concept MVP, I could build the first dataset

## [0.0.1] - 2021-10-24
### Added
- Building up the package
