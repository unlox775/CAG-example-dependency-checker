# Agent Prompts for Dependency Documentation

> **⚠️ AI Generated Prompts**  
> This file contains prompts for AI agents to assist with dependency documentation maintenance.

## Link Validation and Fixing

### Primary Task: Fix Broken Links
When the link validator reports broken links, use the following process:

1. **Run the enhanced link validator**:
   ```bash
   cd docs/dependencies
   python3 validators/enhanced_link_validator.py
   ```

2. **Review the agentic prompt** in `results/agentic-prompt-YYYY-MM-DD.txt`

3. **For each broken link**:
   - If it's a local file issue, use the suggested file paths or search the codebase
   - If it's an external URL issue, use the Google search results to find the correct URL
   - If it's a missing documentation link, add appropriate documentation and GitHub links

4. **Edit the files** to fix the broken links

5. **Re-run the validator** until all links are valid

### Link Validation Standards

#### Required Links for Each Dependency
Every dependency entry must have:
- **Documentation link**: Link to official documentation
- **GitHub link**: Link to source code repository (if available)

#### Link Format Standards
- Local files: `[filename.ext:line](../../path/to/file.ext#L123)`
- External URLs: `[Description](https://example.com)`
- Documentation: `[Docs](https://docs.example.com) | [GitHub](https://github.com/user/repo)`

#### Error Handling
- **404 errors**: Find correct URL or remove link
- **Directory references**: Find actual file in directory
- **Missing files**: Search codebase for similar files
- **Missing documentation**: Add documentation and GitHub links

### Automated Tasks

#### Daily Link Validation
```bash
cd docs/dependencies
make check-links
```

#### Fix Broken Links
```bash
cd docs/dependencies
python3 validators/fix_all_links.py
```

#### Make Links Clickable
```bash
cd docs/dependencies
python3 validators/make_links_clickable.py
```

### Search Strategies

#### For External URLs
1. Extract package name from URL
2. Search Google for "{package_name} documentation"
3. Use top 5 results to find correct URL

#### For Local Files
1. Extract filename from broken path
2. Search codebase for files with similar names
3. Use Levenshtein distance to find closest matches

#### For Missing Documentation
1. Search Google for "{dependency_name} documentation"
2. Search Google for "{dependency_name} github"
3. Add both documentation and GitHub links

### Quality Standards

#### Link Validation Must Pass
- All local file links must exist and have valid line numbers
- All external URLs must return 200 status
- All dependencies must have documentation and GitHub links
- No broken links, warnings, or errors

#### Documentation Quality
- Each dependency entry must be complete
- All links must be clickable and functional
- Documentation must be accurate and up-to-date

### Troubleshooting

#### If Google Search is Blocked
- Check `results/AA_I_AM_BLOCKED.txt` for details
- Use alternative search methods
- Manually research correct URLs

#### If Files Can't Be Found
- Search codebase more broadly
- Check for renamed or moved files
- Update file paths to current structure

#### If Documentation is Missing
- Research the package online
- Find official documentation
- Locate GitHub repository
- Add appropriate links

### Success Criteria

The link validation is successful when:
- ✅ All links are valid (no broken links)
- ✅ All dependencies have documentation links
- ✅ All dependencies have GitHub links
- ✅ No warnings or errors
- ✅ All local file references work correctly

### Maintenance Schedule

- **Daily**: Run link validation
- **Weekly**: Fix any broken links found
- **Monthly**: Review and update documentation links
- **Before commits**: Ensure all links are valid