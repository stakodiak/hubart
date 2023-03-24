# List of days ago
offsets=(9 10 10 11 12 13 18 23 24 25 26 27 41 40 39 38 44 52 53 54 54 55 46 69 68 67 66 65 72 80 74 93 94 95 96 97 102 108 100 121 122 123 130 137 136 135 130 131 132 167 166 165 164 163 171 177 185 191 192 193 194 195 209 208 207 206 212 220 221 222 223 214 233 234 235 236 237 242 250 251 248 240 261 268 262 263 264 265 272 275 279 293 292 291 290 289 298 307 306 305 303 304)

# Find the most recent Sunday prior to or on one year ago from today
reference_date=$(date -u -v-1y -v0w +%Y-%m-%d)

# Create a dummy file if it doesn't exist
touch dummy.txt

# Generate commits with specified offsets
for offset in "${offsets[@]}"; do
  date=$(date -u -j -f "%Y-%m-%d" -v+"${offset}"d "$reference_date" +%Y-%m-%d)
  echo "Commit on $date" >> dummy.txt
  git add dummy.txt
  GIT_AUTHOR_DATE="$date 12:00:00" GIT_COMMITTER_DATE="$date 12:00:00" git commit -m "Commit on $date"
done
