# Change Log

## [v0.0.7](https://github.com/mbeacom/cloudendure-python/tree/v0.0.7) (2019-08-13)
[Full Changelog](https://github.com/mbeacom/cloudendure-python/compare/v0.0.6...v0.0.7)

**Implemented enhancements:**

- Migrate all config items to config module [\#28](https://github.com/mbeacom/cloudendure-python/issues/28)
- Update replication settings to conform to desired KMS usage [\#24](https://github.com/mbeacom/cloudendure-python/issues/24)
- Update main CLI handling to employ defined exceptions/feedback loops [\#6](https://github.com/mbeacom/cloudendure-python/issues/6)
- Add typing throughout and import annotations from future [\#35](https://github.com/mbeacom/cloudendure-python/pull/35) ([mbeacom](https://github.com/mbeacom))
- Update documentation with events entry and logos [\#34](https://github.com/mbeacom/cloudendure-python/pull/34) ([mbeacom](https://github.com/mbeacom))
- Move all configs to use Config for env and yaml [\#33](https://github.com/mbeacom/cloudendure-python/pull/33) ([mbeacom](https://github.com/mbeacom))
- Add base event handler and implementation on launch function [\#32](https://github.com/mbeacom/cloudendure-python/pull/32) ([mbeacom](https://github.com/mbeacom))
- Change image name to avoid blowup [\#26](https://github.com/mbeacom/cloudendure-python/pull/26) ([twarnock2w](https://github.com/twarnock2w))

**Fixed bugs:**

- Bug in update blueprint flow [\#10](https://github.com/mbeacom/cloudendure-python/issues/10)
- Image creation failure [\#9](https://github.com/mbeacom/cloudendure-python/issues/9)
- Share AMI should pull image id from env/config [\#8](https://github.com/mbeacom/cloudendure-python/issues/8)
- Bug in last launch checks in main cli [\#7](https://github.com/mbeacom/cloudendure-python/issues/7)

**Closed issues:**

- Remove 3.6 support and prepare 0.0.7 [\#37](https://github.com/mbeacom/cloudendure-python/issues/37)
- Upgrade docker images to buster [\#36](https://github.com/mbeacom/cloudendure-python/issues/36)
- Event handling - track wave status [\#31](https://github.com/mbeacom/cloudendure-python/issues/31)

**Merged pull requests:**

- Upgrade docker images and drop py3.6 support [\#38](https://github.com/mbeacom/cloudendure-python/pull/38) ([mbeacom](https://github.com/mbeacom))
- update-encryption-key added [\#25](https://github.com/mbeacom/cloudendure-python/pull/25) ([twarnock2w](https://github.com/twarnock2w))
- made image names not 'test' [\#23](https://github.com/mbeacom/cloudendure-python/pull/23) ([twarnock2w](https://github.com/twarnock2w))
- v0.0.6 [\#22](https://github.com/mbeacom/cloudendure-python/pull/22) ([mbeacom](https://github.com/mbeacom))

## [v0.0.6](https://github.com/mbeacom/cloudendure-python/tree/v0.0.6) (2019-08-06)
[Full Changelog](https://github.com/mbeacom/cloudendure-python/compare/v0.0.5...v0.0.6)

**Implemented enhancements:**

- Add python-fire to package dependencies [\#13](https://github.com/mbeacom/cloudendure-python/issues/13)
- copy\_image and split\_image support [\#20](https://github.com/mbeacom/cloudendure-python/pull/20) ([twarnock2w](https://github.com/twarnock2w))
- Add black to makefile [\#18](https://github.com/mbeacom/cloudendure-python/pull/18) ([mbeacom](https://github.com/mbeacom))
- Add typing throughout base project [\#17](https://github.com/mbeacom/cloudendure-python/pull/17) ([mbeacom](https://github.com/mbeacom))
- Check uses replica now.  Launch looks up project\_id and stops on replica. [\#16](https://github.com/mbeacom/cloudendure-python/pull/16) ([twarnock2w](https://github.com/twarnock2w))

**Merged pull requests:**

- Fixed update\_blueprint to actually work [\#21](https://github.com/mbeacom/cloudendure-python/pull/21) ([twarnock2w](https://github.com/twarnock2w))
- Create and share image changes. [\#19](https://github.com/mbeacom/cloudendure-python/pull/19) ([twarnock2w](https://github.com/twarnock2w))
- Update dependencies and adjust formatting [\#15](https://github.com/mbeacom/cloudendure-python/pull/15) ([mbeacom](https://github.com/mbeacom))

## [v0.0.5](https://github.com/mbeacom/cloudendure-python/tree/v0.0.5) (2019-06-28)
[Full Changelog](https://github.com/mbeacom/cloudendure-python/compare/v0.0.4...v0.0.5)

**Implemented enhancements:**

- Add security policy [\#12](https://github.com/mbeacom/cloudendure-python/issues/12)
- Add fire [\#14](https://github.com/mbeacom/cloudendure-python/pull/14) ([mbeacom](https://github.com/mbeacom))

## [v0.0.4](https://github.com/mbeacom/cloudendure-python/tree/v0.0.4) (2019-06-28)
[Full Changelog](https://github.com/mbeacom/cloudendure-python/compare/v0.0.3...v0.0.4)

**Implemented enhancements:**

- Update docstrings, docs, and typing [\#11](https://github.com/mbeacom/cloudendure-python/pull/11) ([mbeacom](https://github.com/mbeacom))

## [v0.0.3](https://github.com/mbeacom/cloudendure-python/tree/v0.0.3) (2019-06-20)
[Full Changelog](https://github.com/mbeacom/cloudendure-python/compare/v0.0.2...v0.0.3)

**Implemented enhancements:**

- Update pip dependencies [\#3](https://github.com/mbeacom/cloudendure-python/pull/3) ([mbeacom](https://github.com/mbeacom))

**Merged pull requests:**

- Update README.md [\#4](https://github.com/mbeacom/cloudendure-python/pull/4) ([twarnock2w](https://github.com/twarnock2w))

## [v0.0.2](https://github.com/mbeacom/cloudendure-python/tree/v0.0.2) (2019-06-16)
[Full Changelog](https://github.com/mbeacom/cloudendure-python/compare/v0.0.1...v0.0.2)

**Implemented enhancements:**

- Pointed API usecase and CLI additions [\#2](https://github.com/mbeacom/cloudendure-python/pull/2) ([mbeacom](https://github.com/mbeacom))

## [v0.0.1](https://github.com/mbeacom/cloudendure-python/tree/v0.0.1) (2019-05-30)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*